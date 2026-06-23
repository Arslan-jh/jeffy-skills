# Interactive HTML Deliverable

## File Requirements

Create a single `.html` file unless the user asks for a web app project. Prefer no build step.

Use `assets/interactive-itinerary-template.html` as the starting point:
- Copy it to the working/output directory.
- Replace the sample `tripData` with destination-specific researched data.
- Keep the interaction model unless the destination requires a better layout.

The page must work by opening the HTML file directly. It may use CDN Leaflet for maps when internet is available. Include a plain list fallback so the itinerary remains usable if map tiles do not load.

## Required Interactions

Include:
- 3/5/7-day switcher.
- Category filters: food, drinks, activities, shopping, lodging, transport, prep.
- Day selector that updates the route, stop list, and cost rollup.
- Dynamic per-person budget calculator with group size and lodging level controls.
- Optional paid activity toggles.
- Clickable place cards with address, phone, official site, booking link, menu link, map link, hours/source link, and notes when available.
- Source panel with last-checked date.

## Map Requirements

Show:
- One total map containing all recommended places.
- A per-day route overlay or ordered stop list for the selected day.
- Distinct marker colors/icons by category.
- Day sequence numbers for daily stops when practical.

Use verified coordinates from maps/geocoding/source pages. If coordinates are unavailable, use map links and do not invent precise pins.

## Data Quality

Every real-world venue should have as many verified fields as possible:
- name
- category
- address
- latitude/longitude when verified
- phone
- officialUrl
- bookingUrl
- menuUrl
- mapUrl
- hoursNote
- priceNote
- why
- caveat
- sources

If a field cannot be verified, leave it blank or write "not found in current public sources"; do not guess.

## Visual Structure

Use a polished travel-dashboard layout:
- Top summary with destination, assumptions, base area, best default duration, and estimated cost.
- Left or top controls for duration, lodging level, group size, and filters.
- Main map section.
- Day-by-day route section.
- Category sections for food, drinks, activities, shopping, lodging, transport, and preparation.
- Source and caveat section at the bottom.

Keep the interface content-dense but comfortable. Avoid decorative filler that does not help the traveler decide.

## Verification Before Delivery

Before final response:
- Open the HTML locally or otherwise verify it exists and renders.
- Check that duration switching changes days and cost.
- Check that filters affect place visibility.
- Check that every major recommendation has a source link or an explicit uncertainty note.
- Report any limitations, such as map tiles requiring internet or menu links unavailable.
