# Steam Player Level Percentiles

This repository contains Python code to query percentiles of player levels, to infer the total number of Steam players.

![Illustration cover][img-cover]

## Requirements

- Install the latest version of [Python 3.X][python-download-url].
- Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```


## Assumption

Let us assume that, in order to compute the percentages, Valve:

- divides the total number of players by 100,
- then truncates it.

For instance, with `16,483,473` players at level 1, and `104,857,600` players in total,
then the percentile would be:
```
16,483,473 / 1,048,576 ~ 15.719864845275879
```

which is finally displayed as:

```
https://api.steampowered.com/IPlayerService/GetSteamLevelDistribution/v1/?player_level=1
```

```json
{
  "response": {
    "player_level_percentile": 15.719864845275879
  }
}
```

## Results

```
Least Common Multiple: 1048576
```

Following our assumption, this would mean that the total number of Steam players is
a multiple of `104,857,6XY`, where `XY` are unknown digits.
This is not super useful info.😅

## Truncation

> **Note**
> Interestingly, the least common multiplier is a power of 2.

$$
1048576 = 1024^2 = 2^{20}
$$

This could indicate a truncation of the numbers in binary code,
which would prevent the estimation of a total number of Steam players
of the order $2^{28} - 2^{30}$, i.e. hundreds of millions.

## References

- [`GetSteamLevelDistribution`][steamdb-api]: API which returns how a given Steam Level compares the user base at large
- Tyler Glaiel, [*Using achievement stats to estimate sales on Steam*][glaiel-medium-blogpost], June 2018
- [`TylerGlaiel/steamsalesestimator`][glaiel-sales-estimator]: C++ code supporting the aforementioned blog post
- Ars Technica's article: [*Valve leaks Steam game player counts; we have the numbers*][article], July 2018
- Ars Technica's supplemental data: [snapshot of "players estimate"][arstechnica18-data] for 13,281 games

<!-- Definitions -->

[img-cover]: <https://github.com/woctezuma/steam-player-level-percentiles/wiki/img/cover.png>
[python-download-url]: <https://www.python.org/downloads/>

[steamdb-api]: <https://steamapi.xpaw.me/#IPlayerService/GetSteamLevelDistribution>
[glaiel-medium-blogpost]: <https://medium.com/@tglaiel/using-achievement-stats-to-estimate-sales-on-steam-d18b4b635d23>
[glaiel-sales-estimator]: <https://github.com/TylerGlaiel/steamsalesestimator>
[article]: <https://arstechnica.com/gaming/2018/07/steam-data-leak-reveals-precise-player-count-for-thousands-of-games/>
[arstechnica18-data]: <http://www.arstechnica.com/wp-content/uploads/2018/07/games_achievements_players_2018-07-01.csv>
