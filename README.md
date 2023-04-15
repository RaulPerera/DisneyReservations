# DisneyReservations
Check for availability at Disney Restaurants

Based on https://dev.to/hmhrex/coding-my-way-into-the-magic-kingdom-1ok2

http://kramnameloc.com/automating-disney

Useful Documntation
https://requests.readthedocs.io/en/latest/user/quickstart/



https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/{D7B825B5-061E-4CD1-8DCC-1950A408F3DC}/wdw/19634138;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00

This was for a June 16th search of Space 2020 at 6pm from https://disneyworld.disney.go.com/dining/epcot/space-220-lounge/availability-modal/

# H1 Examples
# H2 An example for Space 220 that can't find reservations
**URL**
https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/%7BD7B825B5-061E-4CD1-8DCC-1950A408F3DC%7D/wdw/19634138;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00

**Returned Result**
{"error":null,"unavailableReason":"NO_AVAILABILITY","unavailableMessage":{"head":"Sorry!","titleTemplate":"There are no times available between {date} and {date}.","singleDateTitleTemplate":"There are no times available for {date}.","subtitle":"Please select a different date, time or party size--","linkTemplate":"or {link}","linkText":"reserve another restaurant available at this time.","link":"/dining"},"searchRangeMiliseconds":5400000}

# H2 An example for Chefs de France that found reservations
**URL**
https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/%7BD7B825B5-061E-4CD1-8DCC-1950A408F3DC%7D/wdw/90001373;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00
**Returned Result** *This returned 3 start times, 5:40PM, 6PM, and 7pm*
{"error":null,"offers":[{"dateTime":"2023-06-16T17:40:00-04:00","time":"17:40","url":"/dining-reservation/setup-order/table-service/?offerId%5B%5D=https%3A%2F%2Favailability.service.wdprapps.disney.com%2Favailability-service%2Ftable-service-availability%2F23ba714c-ca4c-41ae-b88f-f9107ffd6f4f%2Foffers%2Fa553b2d0-2666-461a-81e1-6c52ea731546"},{"dateTime":"2023-06-16T18:00:00-04:00","time":"18:00","url":"/dining-reservation/setup-order/table-service/?offerId%5B%5D=https%3A%2F%2Favailability.service.wdprapps.disney.com%2Favailability-service%2Ftable-service-availability%2F23ba714c-ca4c-41ae-b88f-f9107ffd6f4f%2Foffers%2F58e5a1a0-1da3-48dd-abb3-a64dcdd7e005"},{"dateTime":"2023-06-16T19:00:00-04:00","time":"19:00","url":"/dining-reservation/setup-order/table-service/?offerId%5B%5D=https%3A%2F%2Favailability.service.wdprapps.disney.com%2Favailability-service%2Ftable-service-availability%2F23ba714c-ca4c-41ae-b88f-f9107ffd6f4f%2Foffers%2Fd174c639-c634-4110-a774-7e1c3705a2ba"}]}

