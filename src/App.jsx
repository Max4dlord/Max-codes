import { HashRouter, Routes, Route, Navigate } from 'react-router-dom'
import { Analytics } from '@vercel/analytics/react'
import Navbar from './components/Navbar.jsx'
import Landing from './components/Landing.jsx'
import Dashboard from './components/Dashboard.jsx'
import TestRunner from './components/TestRunner.jsx'
import StudyRunner from './components/StudyRunner.jsx'
import Results from './components/Results.jsx'

export default function App() {
  return (
    <HashRouter>
      <Navbar />
      <main className="app-main">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/test" element={<TestRunner />} />
          <Route path="/study" element={<StudyRunner />} />
          <Route path="/results" element={<Results />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      <Analytics />
    </HashRouter>
  )
}
