# Travel Planning Framework

## When the User Only Provides a Destination

Proceed with these assumptions:
- Build 3-day, 5-day, and 7-day versions.
- Treat 5 days / 4 nights as the primary recommendation.
- Use a relaxed pace with 2-3 anchors per day.
- Assume mid-range comfort.
- Cover local food, craft beer/cocktails, cafes, citywalk, indoor climbing, hiking/outdoors, local activities, souvenirs, convenient lodging, practical transit, and preparation.

Start the answer or HTML with:
1. "I am assuming..." with duration options, pace, budget band, and traveler type.
2. "The trip logic is..." explaining the neighborhood/route structure.
3. "I would stay in..." naming 1-3 best lodging areas before naming hotels.

## Source Strategy

Use the most relevant current sources for the destination:
- Official: tourism board, city transit, airport/rail, museum/park/trail/venue official pages.
- Maps/reviews: Google Maps, Apple Maps, TripAdvisor, Booking, Agoda, Hotels.com, Expedia, OpenRice, Tabelog, Naver/Kakao, Dianping, Xiaohongshu, Reddit, local forums, as appropriate and accessible.
- Editorial/local: Michelin, Eater, Time Out, local newspapers, local food writers, specialty coffee/cocktail/craft beer guides.
- Practical: exchange-rate sources, government travel advisories where safety/visa/health matters, local weather/climate references.

Prefer recent reviews and official pages for hours, closures, prices, menus, booking rules, and contact details. Use older editorial guides mainly to discover candidates, then verify current status elsewhere.

## Evidence Rules

For each major recommendation, capture:
- What it is best for.
- Why it fits a relaxed local-character trip.
- What sources support it.
- Contact/details when available: official site, phone, address, map link, booking link, menu link, hours source.
- Any tradeoff: crowds, reservation difficulty, price, distance, weather, touristiness, or polarizing reviews.

Use these labels when useful:
- "Core pick": high confidence and central to the plan.
- "Optional swap": good if weather, energy, or interest changes.
- "Only if nearby": worthwhile but not worth a special trip.
- "Skip unless requested": famous but poor fit for relaxed/local travel.

## Duration Logic

3-day plan:
- Prioritize one best lodging base, two signature neighborhoods, one food-market/casual-food cluster, one strong dinner, one drink/cafe cluster, and one citywalk.
- Include hikes or indoor climbing only if they are easy to reach and do not crowd out the destination's core character.

5-day plan:
- Use as the primary route.
- Include balanced citywalks, food/drink depth, one outdoor/hike option, one indoor climbing/local activity option, shopping, and recovery time.

7-day plan:
- Add slower neighborhoods, day trips, workshops, deeper nightlife/drinks, second hike or scenic route, and more local restaurants/cafes.
- Keep the pace relaxed; do not fill every empty slot.

## Itinerary Construction

Design each day as:
- Morning: one main walk, neighborhood, museum, market, or outdoor anchor.
- Afternoon: second anchor plus cafe/rest time.
- Evening: dinner and drink option clustered nearby.

Keep travel-time rules:
- Avoid more than one cross-city transfer per day unless necessary.
- Put hikes/outdoor trips on the clearest weather day if dates are known.
- Put reservation-heavy restaurants and bars earlier in planning notes.
- Treat arrival and departure days as lighter unless the user says they have full days.

## Category Checklist

Food:
- Identify local dishes, market foods, bakeries/snacks, casual meals, one better dinner if appropriate, and reservation notes.
- Recommend what to order, not just where to go.
- Include menu links or official/social menu sources where available.

Drinks:
- Include specialty coffee, craft beer, cocktail bars, wine/sake/tea/local drinks when relevant.
- Mention vibe, booking needs, signature drinks, and alcohol-service caveats.

Activities:
- Include citywalk routes with start/end neighborhoods and map stops.
- Include indoor climbing gyms only after verifying current existence, access, day passes, and location practicality.
- Include hikes with difficulty, transit access, season/weather risk, and safety notes.
- Include local activities such as bathhouses, music venues, workshops, sports, markets, festivals, or neighborhood rituals when relevant.

Shopping:
- Focus on consumable or locally made souvenirs.
- Recommend practical purchase points: markets, department-store food halls, museum shops, independent shops, airports only as fallback.

Lodging:
- Recommend neighborhoods first by convenience, transit, food/drink access, noise, and airport/station access.
- Then list representative hotels or hotel types if current evidence supports them.
- Prefer clean, comfortable, well-located, consistently reviewed properties in a reasonable range.
- State tradeoffs: nightlife noise, business district emptiness, old rooms, tiny rooms, tourist crowds, or weak transit.

Transport:
- Explain arrival/departure route, local transit pass/payment, walking/ride-hailing, taxis, bikes/scooters, car rental if needed, and intercity options.
- Mention last-train or cash-only risks where relevant.

Preparation and practical notes:
- Include currency, rough exchange-rate check, cash/card acceptance, tipping/service charge, power plug, weather/packing, booking windows, local etiquette, safety, and connectivity.
- Include local apps for maps, transit, taxi/ride-hailing, food reservations, translation, payment, and eSIM.
- Include daily phrases with pronunciation when useful: greeting, thanks, excuse me, ordering, allergy/dietary, bill/payment, directions, and emergency.

## Cost Model

Estimate per-person cost with transparent bands:
- Lodging: per room per night divided by group size, with budget/mid/comfort options.
- Food and drinks: per day bands, separating casual meals, better dinners, coffee, bars.
- Activities: fixed optional items that can be toggled.
- Local transport: daily transit/taxi estimate.
- Intercity/day-trip transport: separate line item.
- Shopping: optional planning allowance, not counted by default unless requested.

Use local currency and a user-friendly converted currency when possible. Mark estimates as planning ranges, not quotes.

## Output Skeleton for HTML Data

Structure the data before writing HTML:

```js
const tripData = {
  destination: "",
  currency: "",
  exchangeNote: "",
  durations: {
    3: { title: "", days: [] },
    5: { title: "", days: [] },
    7: { title: "", days: [] }
  },
  places: [],
  costModel: {},
  prep: [],
  apps: [],
  phrases: [],
  sources: []
};
```

Keep the final plan decisive: choose a best plan, then show alternatives only where they improve fit or resilience.
