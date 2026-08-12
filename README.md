# MTH 202 — Mathematical Methods · CBT Lab

A clean, exam-realistic Computer-Based Testing platform. Built with **React + Vite**.
Run it, practice timed/topic-based tests, pause the timer, and review every question
with full worked solutions — all offline, progress auto-saved in the browser.

---

## ▶️ Run it

```bash
cd cbt-platform
npm install      # first time only
npm run dev      # http://localhost:5173
```

Build for production: `npm run build` → deploy the `dist/` folder anywhere.

---

## ✨ Features (what's already working)

- **Landing page** for MTH 202 — Mathematical Methods.
- **Dashboard** to configure each test:
  - Choose **duration** (10–90 min) and **number of questions** (10–50 or all).
  - **Full test** (all topics, shuffled) **or topic-based test** (e.g. *Complex Numbers, 25 min, 40 Q*).
  - Topics are **auto-classified from the question bank** — tag a question with a `topicId` and it appears here.
  - **Course selector** — built to scale to many courses.
- **Test engine**:
  - Live countdown with **Pause / Resume**.
  - **Shuffled** question order on every start; **question palette** to jump/flag.
  - **Auto-saved progress** — reload, close the tab, come back tomorrow and **resume exactly where you stopped** (answers, timer, current question all preserved).
  - Auto-submit when time hits zero.
- **Results & review**:
  - Score ring + breakdown (correct / wrong / skipped / time used).
  - Per question: right/wrong verdict + a **one-line explanation**.
  - **“Show full explanation”** opens a **side panel** with the complete, step-by-step worked solution — **no redirect, no progress lost**.
  - “Expand all explanations” to read everything inline.
- **Multi-course ready** — add courses/topics/questions in one file.

---

## 🗂️ Add YOUR real past questions & solutions

Everything lives in **`src/data.js`**. Each question is one object:

```js
{
  id: 'mth202_c_6',                 // unique
  topicId: 'complex-numbers',       // must exist in topicMeta[mth202]
  question: 'Your question text?',
  options: ['A', 'B', 'C', 'D'],    // 2–6 options
  correct: 2,                       // index of the right option (0-based)
  short: 'One-line why it is right/wrong.',
  solution: 'Full step-by-step worked solution shown in the side panel.'
}
```

**To add questions:** push objects into `questionBank['mth202']` and tag each with a `topicId`.
**To add a topic:** add `{ id, name }` to `topicMeta['mth202']` — it shows on the dashboard automatically.
**To add a course:** add to `courses`, plus `topicMeta[<id>]` and `questionBank[<id>]` arrays.

> The sample bank has ~27 questions across 6 topics (Complex Numbers, Differential
> Equations, Laplace Transforms, Fourier Series, Vector Analysis, PDEs). Replace them
> with your real past questions and the few solutions you already have.

---

## 💬 Optional Telegram integration

The recommended approach (in-app side panel) is already implemented, so **progress is
never disrupted**. If you also want a Telegram community/bot for live discussion:

1. Create a Telegram group/bot, copy its invite link (e.g. `https://t.me/+YourGroup`).
2. Paste it into `TELEGRAM_URL` in **`src/utils.js`**.
3. A **“Discuss in Telegram →”** button then appears inside the solution panel.
   It opens in a **new tab**, so the test/results are never disturbed, and progress
   stays saved — the user returns to the exact same spot.

> The side panel already keeps users in-app, so Telegram is purely a bonus channel.
> If you later want an **on-demand AI solution bot** (for questions you haven't typed
> solutions for), that can be wired into the same panel — replace the `solution` lookup
> with a fetch to your bot/API.

---

## 🧱 Project structure

```
cbt-platform/
  index.html
  vite.config.js
  src/
    main.jsx            app entry
    App.jsx             routes (HashRouter): / /dashboard /test /results
    styles.css          full design system
    data.js             ← YOUR question bank, courses, topics
    utils.js            shuffle, time format, question-set builder, TELEGRAM_URL
    progress.js         localStorage save/resume + results
    components/
      Navbar.jsx        brand + links + "Resume test" indicator
      Landing.jsx       hero, features, how-it-works, topics
      Dashboard.jsx     configure + start/resume tests, bank overview
      Timer.jsx         countdown display + pause/resume control
      TestRunner.jsx    test engine: timer, palette, save, submit
      Results.jsx       score + review + show-full-explanation
      SolutionPanel.jsx side panel with full worked solutions
```

---

## 🛣️ Possible next steps

- Backend + accounts for cross-device progress sync (swap `progress.js` for an API).
- CSV/JSON importer so you can bulk-paste past questions instead of editing JS.
- AI solution-on-demand for questions without a stored solution.
- Analytics (weak topics, average time per question).
