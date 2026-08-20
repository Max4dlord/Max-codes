import { useState, useEffect } from 'react'
import { useNavigate, Navigate, Link } from 'react-router-dom'
import { loadStudySession, saveStudySession } from '../progress.js'

const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']

export default function StudyRunner() {
  const navigate = useNavigate()
  const [session, setSession] = useState(() => loadStudySession())
  const [index, setIndex] = useState(session?.index ?? 0)
  const [showSolution, setShowSolution] = useState(false)
  const [revealed, setRevealed] = useState({}) // track which questions have had explanation opened

  if (!session) return <Navigate to="/dashboard" replace />

  const questions = session.questionSet
  const total = questions.length
  const q = questions[index]

  useEffect(() => {
    if (!session) return
    const next = { ...session, index }
    saveStudySession(next)
    setSession(next)
    setShowSolution(false)
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [index])

  function go(i) {
    if (i < 0 || i >= total) return
    setIndex(i)
  }

  function handleSeeExplanation() {
    setShowSolution(true)
    setRevealed(r => ({ ...r, [q.id]: true }))
  }

  function exitToDashboard() {
    navigate('/dashboard')
  }

  const pct = Math.round(((index + 1) / total) * 100)

  return (
    <div className="test-shell">
      {/* ---------- Top bar - NO TIMER ---------- */}
      <div className="test-topbar" style={{ background: 'linear-gradient(135deg, rgba(37,99,235,0.06), rgba(14,165,233,0.04))' }}>
        <div className="test-meta">
          <div>
            <div className="tm-title">{session.courseCode}{session.topicName ? ` · ${session.topicName}` : ' · Study Mode'} <span style={{ fontSize: 11, background: 'var(--primary)', color: '#fff', padding: '3px 8px', borderRadius: 999, marginLeft: 8, verticalAlign: 'middle' }}>STUDY MODE</span></div>
            <div className="tm-sub">Question {index + 1} of {total} · Correct answer already ticked · No timer</div>
          </div>
        </div>
        <div className="progress-wrap" style={{ minWidth: 180 }}>
          <div style={{ fontSize: 12, color: 'var(--muted)', fontWeight: 600 }}>PROGRESS</div>
          <div className="progress-bar"><div className="progress-fill" style={{ width: `${pct}%` }} /></div>
          <div style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>{index + 1} / {total} · {Object.keys(revealed).length} explanations viewed</div>
        </div>
        <div className="flex gap-8">
          <button className="btn btn-ghost btn-sm" onClick={exitToDashboard}>Exit Study</button>
          <Link to="/dashboard" className="btn btn-primary btn-sm">New Study Set →</Link>
        </div>
      </div>

      {/* ---------- Body ---------- */}
      <div className="test-body">
        <div className="qcard" style={{ borderLeft: '4px solid var(--primary)' }}>
          <div className="qhead">
            <span className="qindex">Study Question {index + 1} / {total}</span>
            <span className="qtopic">{q.topicId ? q.topicId.replace(/-/g, ' ') : 'Mixed topics'}</span>
          </div>
          <div className="qtext">{q.question}</div>

          <div className="options">
            {q.options.map((opt, i) => {
              const isCorrect = i === q.correct
              return (
                <div
                  key={i}
                  className={`option ${isCorrect ? 'selected' : ''}`}
                  style={isCorrect ? { borderColor: 'var(--green)', background: 'var(--green-soft)', cursor: 'default' } : { cursor: 'default', opacity: 0.9 }}
                >
                  <span className="opt-key" style={isCorrect ? { background: 'var(--green)', color: '#fff', borderColor: 'var(--green)' } : {}}>{LETTERS[i]}</span>
                  <span style={{ flex: 1 }}>{opt}</span>
                  {isCorrect && <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--green)', background: '#fff', padding: '3px 8px', borderRadius: 999, border: '1px solid var(--green)' }}>✓ Correct</span>}
                </div>
              )
            })}
          </div>

          {/* Immediate See Explanation button */}
          <div style={{ marginTop: 22, display: 'flex', gap: 12, flexWrap: 'wrap' }}>
            <button className="btn btn-primary" onClick={handleSeeExplanation} style={{ flex: 1, minWidth: 200 }}>
              {showSolution ? '✓ Explanation below — scroll down' : 'See Detailed Explanation →'}
            </button>
            <button className="btn btn-ghost" onClick={() => go(index + 1)} disabled={index === total - 1}>
              Next Question →
            </button>
          </div>

          {/* Inline short hint always visible */}
          <div className="ri-short" style={{ marginTop: 18, background: 'var(--card-2)' }}>
            <strong>Quick tip:</strong> {q.short}
          </div>

          {/* Detailed long explanation - shown inline when requested */}
          {showSolution && (
            <div style={{ marginTop: 18, padding: 20, background: 'linear-gradient(135deg, rgba(37,99,235,0.06), rgba(14,165,233,0.04))', border: '1px solid var(--border)', borderRadius: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
                <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>📖 Study Mode — Very Detailed Explanation</div>
                <span className="qtopic" style={{ background: 'var(--green-soft)', color: 'var(--green)', borderColor: 'rgba(5,150,105,0.2)' }}>Correct: {LETTERS[q.correct]}. {q.options[q.correct]}</span>
              </div>
              <div className="panel-sol" style={{ whiteSpace: 'pre-wrap', background: '#fff' }}>
                {q.solution}

                {/* Extra study-only deep dive - longer than test mode */}
                <div style={{ marginTop: 18, paddingTop: 18, borderTop: '1px dashed var(--border)' }}>
                  <div style={{ fontWeight: 700, color: 'var(--text)', marginBottom: 8 }}>🔍 Deep Dive (Study Mode Extra):</div>
                  <div style={{ fontSize: 14, lineHeight: 1.7, color: 'var(--muted)' }}>
                    This is the <strong>extended Study Mode explanation</strong> — longer than Test Mode. Focus on <em>why</em> the correct answer works and <em>why each distractor fails</em>.
                    {'\n\n'}
                    • <strong>Key idea to remember:</strong> {q.short}
                    {'\n'}
                    • <strong>How to approach similar questions:</strong> Identify the core concept first (see Concept line above), write the relevant formula, substitute the given values step-by-step, and eliminate options that violate the formula or units.
                    {'\n'}
                    • <strong>Common mistake to avoid:</strong> Rushing to pick a familiar-looking option without checking all conditions — the distractors are designed to look plausible if you skip a step.
                    {'\n\n'}
                    <em>Tip: In Study Mode, stay on this question as long as you need. In Test Mode with a timer, you’ll need to apply this same reasoning quickly under time pressure.</em>
                  </div>
                </div>
              </div>
              <div style={{ marginTop: 14, display: 'flex', gap: 10 }}>
                <button className="btn btn-ghost btn-sm" onClick={() => setShowSolution(false)}>Hide explanation</button>
                <button className="btn btn-primary btn-sm" onClick={() => go(index + 1)} disabled={index === total - 1}>Next →</button>
              </div>
            </div>
          )}

          <div className="qnav" style={{ marginTop: 24, borderTop: '1px solid var(--border)', paddingTop: 16 }}>
            <button className="btn btn-ghost" onClick={() => go(index - 1)} disabled={index === 0}>← Previous</button>
            <span style={{ fontSize: 12, color: 'var(--muted)' }}>Study Mode · No timer · Correct already ticked</span>
            {index < total - 1 ? (
              <button className="btn btn-primary" onClick={() => go(index + 1)}>Next →</button>
            ) : (
              <button className="btn btn-ghost" onClick={exitToDashboard}>Back to Dashboard</button>
            )}
          </div>
        </div>

        {/* ---------- Palette - Study variant ---------- */}
        <div className="palette">
          <h4>Study Navigator</h4>
          <div className="palette-grid">
            {questions.map((qq, i) => {
              const cls = [
                'pcell',
                revealed[qq.id] ? 'answered' : '',
                i === index ? 'current' : ''
              ].filter(Boolean).join(' ')
              return (
                <button key={qq.id} className={cls} onClick={() => go(i)} title={`Question ${i + 1} ${revealed[qq.id] ? '(viewed)' : ''}`}>
                  {i + 1}
                </button>
              )
            })}
          </div>
          <div className="palette-legend">
            <span><span className="legend-dot" style={{ background: 'var(--green-soft)', border: '1px solid rgba(5,150,105,0.4)' }} />Viewed</span>
            <span><span className="legend-dot" style={{ background: 'var(--primary)' }} />Current</span>
          </div>
          <div style={{ marginTop: 18, padding: 12, background: 'var(--primary-soft)', borderRadius: 10, border: '1px solid rgba(37,99,235,0.12)' }}>
            <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--primary)' }}>💡 How Study Mode works</div>
            <div style={{ fontSize: 12, color: 'var(--muted)', marginTop: 6, lineHeight: 1.5 }}>
              No timer. Correct answer is pre-ticked in green. Tap <strong>See Detailed Explanation</strong> for the very long, step-by-step breakdown — longer than Test Mode.
            </div>
          </div>
          <p className="muted" style={{ fontSize: 12, marginTop: 12, lineHeight: 1.5 }}>
            Go at your own pace. No auto-save timer, no pressure.
          </p>
        </div>
      </div>
    </div>
  )
}
