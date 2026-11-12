# Project Overview
This is a consultancy project for a hobbist permacultural in northern Buenos Aires, Argentina.
We provide advice and suggestions regarding ongoing projects.
Not just to answer questions on the fly, but also to help build a body of knowledge tailored to the user context he can revisit and review later on.
The overall strategy is to aim within reasonable parameters for self-sufficiency, avoiding if possible relying on industrial chemical inputs: however this is not a fully "prepper" situation, and it is acceptable to go for some supplies if the output warrants it.

# Backlog
We will not have a specific linear backlog for the project as a whole, since this is a sort of life companion dynamic.
We will have a sort of yearly live calendar where we group high level tasks that are necessary, and we must draw from that list on any conversation to add items there, or to remind the user that he should get some of those done soon.
The expected usage is that the user will launch this project at least once per week as a refresher of what he could do next, get suggestions based on the season, note down what he has done, and let the system re organize the living backlog
- Living backlog file: [backlog.md](backlog.md) — garden to-dos, seasonal care notes, **active multi-session workstreams** (LoRa, irrigation, greenhouse, mesh tunnels) and open project ideas. Check this on any "what should I focus on" style prompt, and surface in-flight workstreams proactively when relevant (check pending-questions files when resuming).


# Homestead specs
The terrain is around 2000 squared meters.
Location: Loma Verde, Escobar (open pampas countryside, north of Buenos Aires)
Latitude: -34.346692535527566
Longitude: -58.83940896971598
Power is on-grid, although in the future some solar panels may be installed
Water comes from a well inside the property, there is no real concern of scarcity in that regard.
Projects with a 3D model keep it in a `models/` folder inside the project folder (Blender, built from parametric scripts); before discussing such a project (e.g. the chicken coop), look at its latest renders and keep them current when the design changes (see the project file for the list; the chicken coop lives in `chicken_coop/` and is at v6 → `chicken_coop/models/renders_v6/`, older versions stay frozen in `chicken_coop/models/renders/`, `renders_v2/` … `renders_v5/` for history).
There is a separate "fruit_trees.md" file with more information on the current layout and rooster of trees that are being cared for.
There will be other separate files such as "vegetable_patches.md", "chicken_coop/chicken_coop.md", etc... where the current status will be reflected (what was planted, when) plus other historical references for those projects


# Folder structure
Major projects have their own subfolder for tracking (the chicken coop already does: `chicken_coop/` holds its md files, models, renders, reference PDFs),  but at a root level of the project we will generate new reports and files for individual topics such as "ash usage for fertilizer", or "banana tea preparation" that will contain summaries of the recommendations for those topics.
We don't have any structural constraint, and the file structure may evolve over time
Files named `*_archive.md` (e.g. `chicken_coop/chicken_coop_archive.md`) hold outdated designs kept only as a human archive: never use them as a source of truth for specs, quantities or shopping lists.


# Logging
During every conversation, key memories must be stored in some files for easier retrieval. We don't need to store every decision made, but we must ensure a library of knowledge is persisted for future reference


# Mobile dashboard (GitHub Pages)
`index.html` at the repo root is the main dashboard, served via GitHub Pages and read from the user's phone (repo: github.com/bonesao/rancho_claude). It shows this week's tasks, upcoming items, things to keep in mind, active projects and links to the working files.
- **Always keep it current.** Whenever `backlog.md` changes, or a conversation adds/completes a task, changes season-relevant advice, or moves a workstream, update `index.html` in the same session (bump its "last updated" date; if the tick-state `key` in its script is tied to the date, change it only when the checklist items change).
- **Git is now Claude's job** (this reverses the earlier "I'll handle the GitHub commits myself" rule): at the end of any session that changed files, commit the changes and push to `main` so the Pages site updates. Stage specific files rather than `git add -A` (untracked media like `november_11.mp4` should not be committed unless asked). Never force-push.
- Keep the page self-contained (inline CSS/JS, no external assets), mobile-first, and short: it is a glanceable summary, not a copy of the md files.
