import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { courses } from '../data.js'
import { getTopics, getQuestionCount, buildQuestionSet } from '../utils.js'
import { loadSession, clearSession, saveSession } from '../progress.js'

const DURATIONS = [10, 15, 20, 25, 30, 45, 60, 90]
const COUNTS = [10, 20, 30, 40, 50, 'all']

export default function Dashboard() {
  const navigate = useNavigate()
  const existing = loadSession()

  const [courseId, setCourseId] = useState(courses.find((c) => c.available)?.id || courses[0].id)
  const [mode, setMode] = useState('full') // 'full' | 'topic'
  const [topicId, setTopicId] = useState(null)
  const [duration, setDuration] = useState(25)
  const [count, setCount] = useState(20)
  const [error, setError] = useState('')

  const course = courses.find((c) => c.id === courseId)
  const topics = getTopics(courseId)
  const poolSize = mode === 'topic' && topicId ? getQuestionCount(courseId, topicId) : getQuestionCount(courseId)
  const selectedTopic = topics.find((t) => t.id === topicId)

  function startTest() {
    setError('')
    if (!course.available) {
      setError('This course is coming soon. Please check back later or choose an available course.')
      return
    }
    if (mode === 'topic' && !topicId) {
      setError('Please pick a topic to start a topic-based test.')
      return
    }
    const set = buildQuestionSet(courseId, {
      mode,
      topicId: mode === 'topic' ? topicId : null,
      count
    })
    if (set.length === 0) {
      setError('No questions available for this selection. Please try another topic.')
      return
    }

    const session = {
      v: 1,
      courseId,
      courseCode: course.code,
      courseTitle: course.title,
      topicId: mode === 'topic' ? topicId : null,
      topicName: mode === 'topic' ? selectedTopic?.name : null,
      mode,
      durationSec: duration * 60,
      remainingSec: duration * 60,
      index: 0,
      answers: {},
      flagged: [],
      paused: false,
      questionSet: set,
      startedAt: Date.now()
    }
    saveSession(session)
    navigate('/test')
  }

  function resumeExisting() {
    if (existing) navigate('/test')
  }
  function discardExisting() {
    clearSession()
    window.location.reload()
  }

  return (
    <div className="page">
      <div className="page-head">
        <h1>Test Dashboard</h1>
        <p>Configure your CBT practice session — choose a duration, the number of questions, and whether to test a single topic or the whole course.</p>
      </div>

      {existing && (
        <div className="resume-banner">
          <div className="r-info">
            <span className="r-ico">⏸️</span>
            <div>
              <div className="r-title">You have a test in progress</div>
              <div className="r-sub">
                {existing.courseCode}{existing.topicName ? ` · ${existing.topicName}` : ' · Full course'} ·
                {' '}{existing.questionSet.length} questions · {existing.index + 1} answered ·
                {' '}{Math.floor(existing.remainingSec / 60)} min left{existing.paused ? ' · paused' : ''}
              </div>
            </div>
          </div>
          <div className="flex gap-8">
            <button className="btn btn-primary btn-sm" onClick={resumeExisting}>Resume →</button>
            <button className="btn btn-danger btn-sm" onClick={discardExisting}>Discard</button>
          </div>
        </div>
      )}

      <div className="grid-2">
        {/* ---- Configuration ---- */}
        <div className="card">
          <h2>1 · Configure your test</h2>

          <div className="field">
            <label>Course</label>
            <div className="course-select-wrap">
              <select value={courseId} onChange={(e) => { setCourseId(e.target.value); setTopicId(null); setMode('full') }}>
                {courses.map((c) => (
                  <option key={c.id} value={c.id}>{c.code} — {c.title}{c.available ? '' : ' (soon)'}</option>
                ))}
              </select>
              <div className="course-pill">
                <span className="course-dot" style={{ background: course.accent }} />
                <span className="muted" style={{ fontSize: 13 }}>{course.available ? 'Available' : 'Coming soon'}</span>
              </div>
            </div>
            <p className="info-line">{course.blurb}</p>
          </div>

          <div className="field">
            <label>Test mode</label>
            <div className="tabs">
              <button className={`tab ${mode === 'full' ? 'active' : ''}`} onClick={() => setMode('full')}>Full test (all topics)</button>
              <button className={`tab ${mode === 'topic' ? 'active' : ''}`} onClick={() => setMode('topic')}>Topic-based test</button>
            </div>
          </div>

          {mode === 'topic' && (
            <div className="field">
              <label>Pick a topic</label>
              <div className="topic-grid">
                {topics.map((t) => (
                  <button
                    key={t.id}
                    className={`topic-chip ${topicId === t.id ? 'selected' : ''}`}
                    onClick={() => setTopicId(t.id)}
                  >
                    <div className="t-name">{t.name}</div>
                  </button>
                ))}
              </div>
            </div>
          )}

          <div className="row">
            <div className="field">
              <label>Duration (minutes)</label>
              <select value={duration} onChange={(e) => setDuration(Number(e.target.value))}>
                {DURATIONS.map((d) => <option key={d} value={d}>{d} min</option>)}
              </select>
            </div>
            <div className="field">
              <label>Number of questions</label>
              <select value={count} onChange={(e) => {
                const v = e.target.value
                setCount(v === 'all' ? 'all' : Number(v))
              }}>
                {COUNTS.map((c) => <option key={String(c)} value={c}>{c === 'all' ? 'All available' : `${c} questions`}</option>)}
              </select>
            </div>
          </div>

          <p className="info-line">
            {mode === 'topic' && topicId
              ? <>Pool for <strong>{selectedTopic?.name}</strong>: <strong>{poolSize}</strong> question(s) available.</>
              : <>Full course pool: <strong>{poolSize}</strong> question(s) available.</>}
            {' '}Questions will be shuffled on start.
          </p>

          {error && <p style={{ color: 'var(--red)', fontSize: 14, marginTop: 12 }}>{error}</p>}

          <div style={{ marginTop: 20 }}>
            <button className="btn btn-primary btn-lg" onClick={startTest} style={{ width: '100%' }}>
              Start {mode === 'topic' ? 'topic' : 'full'} test →
            </button>
          </div>
          <p className="hint">
            Tip: your test auto-saves as you go. Close the tab or refresh and you'll resume exactly where you stopped.
          </p>
        </div>

        {/* ---- Summary / scaling ---- */}
        <div className="card">
          <h2>Overview</h2>
          <p className="muted" style={{ fontSize: 14 }}>
            {course.code} currently has <strong style={{ color: 'var(--text)' }}>{getQuestionCount(courseId)}</strong> total questions
            across <strong style={{ color: 'var(--text)' }}>{topics.length}</strong> topic categories.
          </p>

          <h2 style={{ marginTop: 28, fontSize: 18 }}>Topic categories</h2>
          <div className="topic-grid" style={{ marginTop: 8 }}>
            {topics.map((t) => (
              <div key={t.id} style={{ padding: 14, borderRadius: 12, background: 'var(--bg-soft)', border: '1px solid var(--border)' }}>
                <div style={{ fontWeight: 700, fontSize: 14 }}>{t.name}</div>
              </div>
            ))}
          </div>

          <Link to="/" className="btn btn-ghost btn-sm" style={{ marginTop: 24 }}>← Back to home</Link>
        </div>
      </div>
    </div>
  )
}
