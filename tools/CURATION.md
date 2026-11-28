# How the art wall's picture list is kept

The wall shows only pictures listed in `picks.js`. Every one passed a separate review against the bar below.
Working files live outside the repo, in the project folder `/mnt/project-files/tv-art-live/curation/`.

## The bar

`curation/bar.md` holds the 7-point bar. The build script copies it to the top of `picks.js`.

## Files in the curation folder

- `candidates*.txt`: Stage 1 finds, `File title | cat | tags`.
- `review-batches*.txt`: contact-sheet links, 12 candidates each, for the reviewer.
- `pass*.txt`: Stage 2 passes, `File title | cat | tags | x,y` (x,y is the crop focus in percent of the full frame).
- `pass-paint.txt`: the paintings (famous public-domain works only, about 15 to 20 percent of the wall).
- `fail-log*.txt`: every fail with its reason. Never re-propose a title that is in a fail log.
- `rotation-log.txt`: what each weekly swap retired and added.

Categories: land, water, sea, city, arch, abst, flora, paint.
Tags (space-separated): night, sunrise, sunset, evening, morning, fog, snow, winter, summer, autumn, spring, storm, rain, bw.
Use sunrise and sunset only when the sun or its glow is at the horizon. The page shows those only within an hour of Brea's real sunrise or sunset.

## Two stages, two separate agents

1. **Find (Stage 1).** Search Commons through the contact sheet
   `https://gerhart07.github.io/Art/tools/pick.html?p=1&q=<url-encoded Commons search>`
   (for example `incategory:Featured_pictures_on_Wikimedia_Commons fjord fileh:>2000`).
   Skip anything already in a pass or fail file. No place more than 3 times across all passes.
   Write the new candidates and their review-batch links (`pick.html?big=1&t=<titles joined by %7C>`).
2. **Review (Stage 2).** A different agent opens each batch, sees the full frame and the 9:16 crop,
   and writes PASS with a focus point or FAIL with a reason. Expect to fail a good share.

## Build and publish

```
python3 tools/build-picks.py /mnt/project-files/tv-art-live/curation/pass.txt \
  /mnt/project-files/tv-art-live/curation/pass2.txt \
  /mnt/project-files/tv-art-live/curation/pass-paint.txt > picks.js
```

The first file must sit in the curation folder, because the script reads `bar.md` from there.
Duplicate titles are dropped (the first one wins). Commit `picks.js`, push to `main`, and open
`https://gerhart07.github.io/Art/` to confirm the new count shows.

## Weekly swap (target about 200 picks)

Retire about 20 picks (move their lines from the pass files to `retired.txt` with the date) and add about 20
newly reviewed passes, keeping the category mix: landscapes about half, paintings 15 to 20 percent.
Prefer retiring the oldest picks and any the owner marked "never again". Log both lists in `rotation-log.txt`.

## How the page plays them

The page deals the list like a shuffled deck: every pick shows once before any repeats.
At the default 90 seconds a picture, 200 picks take about 5 hours to cycle.
