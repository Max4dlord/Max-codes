// Data-bank validator for Max-codes CBT Lab.
// Usage: npm run validate
// Hard-checks question-bank integrity and warns about answer-marker
// phrases ("Option A", "correct answer is B"…) that may drift if options
// are ever reordered.

import { existsSync } from 'fs'
import { courses, topicMeta, questionBank } from '../src/data.js'

const errors = []
const warnings = []
const LETTERS = ['A', 'B', 'C', 'D', 'E', 'F']
let total = 0

for (const course of courses) {
  const bank = questionBank[course.id] || []
  const topicIds = new Set((topicMeta[course.id] || []).map((t) => t.id))
  const seen = new Set()
  let ok = 0

  for (const q of bank) {
    total++
    const tag = `${course.id}/${q.id}`
    if (seen.has(q.id)) errors.push(`${tag}: duplicate id`)
    seen.add(q.id)
    if (!q.question || !String(q.question).trim()) errors.push(`${tag}: empty question`)
    if (!Array.isArray(q.options) || q.options.length < 2 || q.options.length > 6)
      errors.push(`${tag}: options must be 2–6, got ${q.options?.length}`)
    if (typeof q.correct !== 'number' || q.correct < 0 || q.correct >= (q.options?.length || 0))
      errors.push(`${tag}: 'correct' index out of range (${q.correct})`)
    if (!q.short || String(q.short).trim().length < 3) errors.push(`${tag}: missing 'short'`)
    if (!q.solution || String(q.solution).trim().length < 5) errors.push(`${tag}: missing 'solution'`)
    if (!q.topicId || !topicIds.has(q.topicId)) errors.push(`${tag}: unknown topicId '${q.topicId}'`)
    if (q.image) {
      const path = './public' + q.image
      if (!existsSync(path)) errors.push(`${tag}: missing image file ${q.image}`)
    }
    // ---- answer-marker heuristic (warnings only) ----
    const text = `${q.short}\n${q.solution}`
    const sentences = text.split(/(?<=[.!?])\s+/)
    const asserted = new Set()
    for (const L of LETTERS) {
      // explicit assertions anywhere in the text
      if (new RegExp(`(?:correct\\s+answer\\s+is|correct\\s+option|answer)\\s*[:–—-]?\\s*${L}\\b`, 'i').test(text))
        asserted.add(L)
      for (const s of sentences) {
        // sentence mentions this option letter AND claims correctness
        if (!/\bcorrect\b|\bis\s+true\b/i.test(s)) continue
        if (!new RegExp(`\\b(?:option|answer)\\s*${L}\\b|\\b${L}\\b[^.!?]*\\bis\\s+correct`, 'i').test(s)) continue
        // but skip if the sentence actually says it is NOT correct
        if (/\b(?:in|not)\s*correct\b|incorrect\b|is\s+wrong\b/i.test(s)) continue
        asserted.add(L)
      }
    }
    if (asserted.size === 1 && !asserted.has(LETTERS[q.correct]))
      warnings.push(`${tag}: answer text claims "${[...asserted]}" is correct but correct=${q.correct} (${LETTERS[q.correct]})`)
    else if (asserted.size > 1 && !asserted.has(LETTERS[q.correct]))
      warnings.push(`${tag}: ambiguous answer text (${[...asserted]}) vs correct=${q.correct} (${LETTERS[q.correct]})`)

    const optsOK = q.options.every((o) => typeof o === 'string' && o.trim().length > 0)
    if (!optsOK) errors.push(`${tag}: empty option string`)
    ok++
  }
  console.log(`${course.code} (${course.id}): ${ok} questions — ${course.available ? 'live' : 'draft'}`)
}

console.log(`\nTotal questions checked: ${total}`)
if (warnings.length) console.log(`\n⚠️  ${warnings.length} warning(s):\n  ` + warnings.slice(0, 20).join('\n  '))
if (errors.length) {
  console.error(`\n❌ ${errors.length} error(s):\n  ` + errors.slice(0, 40).join('\n  '))
  process.exit(1)
} else {
  console.log('\n✅ Bank is valid.')
}
