// ---------------------------------------------------------------------------
// LocalStorage helpers for saving / resuming an in-progress test session.
// This is what powers the "resume exactly where you stopped" feature and the
// pause/start timer. Everything lives in the browser, so it works offline and
// needs no backend. Swap this out for an API later if you want cross-device sync.
// ---------------------------------------------------------------------------

const SESSION_KEY = 'cbt_session_v1'
const RESULTS_KEY = 'cbt_results_v1'

export function saveSession(session) {
  try {
    localStorage.setItem(SESSION_KEY, JSON.stringify(session))
  } catch (e) {
    console.warn('Could not save session:', e)
  }
}

export function loadSession() {
  try {
    const raw = localStorage.getItem(SESSION_KEY)
    return raw ? JSON.parse(raw) : null
  } catch (e) {
    return null
  }
}

export function clearSession() {
  localStorage.removeItem(SESSION_KEY)
}

export function saveResults(results) {
  try {
    localStorage.setItem(RESULTS_KEY, JSON.stringify(results))
  } catch (e) {
    console.warn('Could not save results:', e)
  }
}

export function loadResults() {
  try {
    const raw = localStorage.getItem(RESULTS_KEY)
    return raw ? JSON.parse(raw) : null
  } catch (e) {
    return null
  }
}

export function clearResults() {
  localStorage.removeItem(RESULTS_KEY)
}

const STUDY_KEY = 'cbt_study_v1'

export function saveStudySession(session) {
  try {
    localStorage.setItem(STUDY_KEY, JSON.stringify(session))
  } catch (e) {
    console.warn('Could not save study session:', e)
  }
}

export function loadStudySession() {
  try {
    const raw = localStorage.getItem(STUDY_KEY)
    return raw ? JSON.parse(raw) : null
  } catch (e) {
    return null
  }
}

export function clearStudySession() {
  localStorage.removeItem(STUDY_KEY)
}
