# DisneyReservations
Check for availability at Disney Restaurants

Based on https://dev.to/hmhrex/coding-my-way-into-the-magic-kingdom-1ok2

http://kramnameloc.com/automating-disney

Useful Documntation
https://requests.readthedocs.io/en/latest/user/quickstart/



https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/{D7B825B5-061E-4CD1-8DCC-1950A408F3DC}/wdw/19634138;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00

This was for a June 16th search of Space 2020 at 6pm from https://disneyworld.disney.go.com/dining/epcot/space-220-lounge/availability-modal/

**URL**
https://disneyworld.disney.go.com/finder/api/v1/explorer-service/dining-availability/%7BD7B825B5-061E-4CD1-8DCC-1950A408F3DC%7D/wdw/19634138;entityType=restaurant/table-service/1/2023-06-16/?searchTime=18:00:00

**Returned Result**
{"error":null,"unavailableReason":"NO_AVAILABILITY","unavailableMessage":{"head":"Sorry!","titleTemplate":"There are no times available between {date} and {date}.","singleDateTitleTemplate":"There are no times available for {date}.","subtitle":"Please select a different date, time or party size--","linkTemplate":"or {link}","linkText":"reserve another restaurant available at this time.","link":"/dining"},"searchRangeMiliseconds":5400000}