---
name: travel-planner
description: Evidence-based leisure travel planning with an interactive HTML deliverable. Use when the user asks to plan a trip, itinerary, travel guide, food/drink guide, map route, citywalk, hiking, local activities, souvenirs, lodging areas, transportation, exchange-rate/practical notes, or asks only "I am going to X, how should I plan?" Defaults to a relaxed non-rushed 5-day trip, with switchable 3/5/7-day versions, dynamic per-person cost estimates, route maps, real restaurants/cafes/bars/venues, contact/menu/source links, and preparation notes unless the user specifies another format, style, duration, budget, season, companions, or constraints.
---

# Travel Planner

## Defaults

Use this skill to produce practical travel plans grounded in current public information and real user reviews.

Default assumptions when the user only provides a destination:
- Duration options: build 3-day, 5-day, and 7-day versions; make 5 days the primary recommendation.
- Pace: relaxed, not "special-forces" travel; normally 2-3 meaningful anchors per day plus flexible food/drink stops.
- Goal: maximize local character across food, drinks, activities, walking routes, outdoor options, shopping, lodging convenience, transport, preparation, and practical notes.
- Budget: reasonable mid-range unless the user specifies luxury, budget, backpacking, family, business, or special constraints.
- Deliverable: create a polished interactive single-file HTML artifact unless the user explicitly asks for text only.
- Delivery: after creating a file artifact, send one copy through Feishu by default when lark-cli/Feishu delivery is available; verify the message_id, file upload result, or Drive URL before claiming delivery.
- Output language: match the user's language.

Ask a clarifying question only when the destination is ambiguous, the user needs bookings for fixed dates, or a missing constraint materially changes the plan. Otherwise state the assumptions and proceed.

## Research Workflow

1. Confirm the planning frame:
   - Destination scope, dates or season if given, party type, arrival/departure points, budget signals, mobility limits, dietary needs, and must-do/must-avoid items.
   - If absent, use the defaults above.

2. Browse current public sources before recommending:
   - Official tourism/transport/venue pages for hours, closures, reservation rules, ticketing, trail status, transit passes, and safety notes.
   - Review and map platforms for current user sentiment, recurring praise/complaints, wait times, cleanliness, neighborhood convenience, and value.
   - Local food/drink guides, reputable editorial lists, local blogs/forums, and region-specific platforms when relevant.
   - Recent social or community discussion can inform vibe, but do not treat isolated viral posts as proof.

3. Cross-check every major recommendation:
   - Prefer places that appear in multiple source types or have strong official/current evidence plus consistent review patterns.
   - Flag uncertainty when information is thin, seasonal, language-limited, or review data is polarized.
   - Never invent opening hours, prices, reservation rules, ratings, coordinates, phone numbers, menus, hotel availability, or route timings.

4. Build 3/5/7-day variants:
   - Design each duration separately around the best geographic clusters and priority tradeoffs.
   - Do not merely truncate the 5-day plan for 3 days or pad it for 7 days.
   - Make the 3-day version concentrate on highest-signal local experiences.
   - Make the 5-day version the best balanced plan.
   - Make the 7-day version add slower neighborhoods, hikes/day trips, workshops, nightlife, and deeper local food/drink.

5. Verify practical feasibility:
   - Check travel time between anchors, likely opening days, reservation needs, weather/season risks, and last-train/ride-hailing constraints where relevant.
   - For lodging, recommend areas first, then representative hotel types or examples only if current sources support them.

Read `references/planning-framework.md` for full itinerary rules. Read `references/interactive-html.md` before creating the HTML deliverable. Use `assets/interactive-itinerary-template.html` as the starting template unless a custom app structure is clearly better.

## Required Deliverable

For a normal full-plan request, create an interactive HTML file and give the user its local path. The HTML must include:
- Duration switcher for 3, 5, and 7 days.
- Dynamic per-person total cost estimate that updates when duration, lodging level, group size, and optional paid activities change.
- Category sections matching the user's taxonomy: food, drinks, activities, shopping, lodging, transport, and other/practical prep.
- A total map with all recommended places and color/category markers.
- Day-by-day route views showing that day's line/sequence and stops.
- Real restaurants, cafes, bars, attractions, shops, hotels/areas, transit options, hikes, and climbing gyms where applicable.
- Contact fields where available: official site, phone, address, booking link, map link, menu link, opening hours/source link.
- Source notes and last-checked date for important claims.
- Preparation checklist: reservations, tickets, documents/visa, payments/cash, local apps, connectivity, packing, weather, etiquette, safety, and simple daily phrases.

Also include a short chat summary after creating the file:
- File path.
- Feishu delivery result when available, or the exact blocker if delivery was not possible.
- Default recommendation and why.
- Any important uncertainty or booking caveat.
- Verification performed.

If the user asks for a shorter answer or text-only plan, compress the output, but preserve source-based feasibility checks.

## Recommendation Standards

Prioritize:
- Distinctive local character over generic top-10 sightseeing.
- Places with current, consistent public evidence.
- Clean logistics: short transfers, sensible neighborhood clustering, and fallback options.
- Comfort and recovery time.
- Memorable meals and drinks that reflect the destination.
- Explicit tradeoffs: cost, crowds, booking difficulty, distance, weather risk, and touristiness.

Avoid:
- Overpacked days.
- Recommendations based only on a single influencer/social post.
- Fake precision: do not fabricate coordinates, prices, menus, phone numbers, or hours.
- Luxury hotels or fine dining unless requested.
- Unsafe trails, closed venues, or outdated transport advice.
- Saying "best" without explaining evidence and tradeoff.
