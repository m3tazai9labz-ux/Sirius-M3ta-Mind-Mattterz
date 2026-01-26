# Sirius-M3ta-Mind-Mattterz 🌙✨

## MoonStruck Astrology

A comprehensive astrology module for cosmic insights, moon phases, zodiac signs, and astrological wisdom.

Inspired by [@moonstruckimmemorial](https://www.tiktok.com/@moonstruckimmemorial) 🔮

## Features

- 🌙 **Moon Phase Calculations**: Real-time moon phase tracking with illumination percentages
- ♈︎ **Zodiac Sign Determination**: Accurate zodiac sign calculation based on birth dates
- 🔮 **Daily Insights**: Personalized astrological insights for each zodiac sign
- 💕 **Compatibility Analysis**: Relationship compatibility between zodiac signs
- 📊 **Birth Chart Summaries**: Comprehensive birth chart information including elements and ruling planets
- ✨ **All 12 Zodiac Signs**: Complete coverage of Aries through Pisces

## Installation

No external dependencies required! Just Python 3.6+

```bash
python3 moonstruck_astrology.py
```

## Usage

### Quick Start

```python
from moonstruck_astrology import MoonStruckAstrology
import datetime

# Create an astrology instance
astrology = MoonStruckAstrology()

# Get current moon phase
moon_phase, illumination = astrology.get_moon_phase()
print(f"Current Moon: {moon_phase} ({illumination}% illuminated)")

# Determine zodiac sign
birth_date = datetime.date(1990, 7, 15)
sign = astrology.get_zodiac_sign(birth_date)
print(f"Zodiac Sign: {sign}")

# Get zodiac information
info = astrology.get_zodiac_info(sign)
print(f"Element: {info['element']}")
print(f"Ruling Planet: {info['ruling_planet']}")
print(f"Traits: {', '.join(info['traits'])}")

# Get daily insight
insight = astrology.get_daily_insight(sign)
print(insight)

# Check compatibility
compatibility = astrology.get_compatibility("Cancer", "Pisces")
print(f"Compatibility Score: {compatibility['score']}/100")
```

### Available Methods

#### `get_zodiac_sign(birth_date)`
Returns the zodiac sign for a given birth date.

#### `get_moon_phase(date=None)`
Calculates the current moon phase and illumination percentage.

#### `get_zodiac_info(sign)`
Returns detailed information about a zodiac sign including:
- Element (Fire, Earth, Air, Water)
- Ruling Planet
- Key Traits
- Unicode Symbol

#### `get_compatibility(sign1, sign2)`
Analyzes compatibility between two zodiac signs based on elemental harmony.

#### `get_daily_insight(sign, date=None)`
Generates personalized daily astrological guidance.

#### `get_birth_chart_summary(birth_date)`
Creates a comprehensive birth chart summary.

## Zodiac Signs

| Sign | Symbol | Element | Dates | Ruling Planet |
|------|--------|---------|-------|---------------|
| Aries | ♈︎ | Fire | Mar 21 - Apr 19 | Mars |
| Taurus | ♉︎ | Earth | Apr 20 - May 20 | Venus |
| Gemini | ♊︎ | Air | May 21 - Jun 20 | Mercury |
| Cancer | ♋︎ | Water | Jun 21 - Jul 22 | Moon |
| Leo | ♌︎ | Fire | Jul 23 - Aug 22 | Sun |
| Virgo | ♍︎ | Earth | Aug 23 - Sep 22 | Mercury |
| Libra | ♎︎ | Air | Sep 23 - Oct 22 | Venus |
| Scorpio | ♏︎ | Water | Oct 23 - Nov 21 | Pluto |
| Sagittarius | ♐︎ | Fire | Nov 22 - Dec 21 | Jupiter |
| Capricorn | ♑︎ | Earth | Dec 22 - Jan 19 | Saturn |
| Aquarius | ♒︎ | Air | Jan 20 - Feb 18 | Uranus |
| Pisces | ♓︎ | Water | Feb 19 - Mar 20 | Neptune |

## Moon Phases

The module calculates 8 distinct moon phases:
- 🌑 New Moon
- 🌒 Waxing Crescent
- 🌓 First Quarter
- 🌔 Waxing Gibbous
- 🌕 Full Moon
- 🌖 Waning Gibbous
- 🌗 Last Quarter
- 🌘 Waning Crescent

## Examples

### Example Output

```
✨ Welcome to MoonStruck Astrology ✨
==================================================

🌙 Current Moon Phase: Waxing Gibbous 🌔
   Illumination: 78.3%

📅 Example Birth Date: July 15, 1990
♈︎ Zodiac Sign: Cancer

🔮 Cancer Information:
   Element: Water
   Ruling Planet: Moon
   Traits: tenacious, loyal, emotional, sympathetic

💫 Daily Insight:
   ♋︎ Cancer - The Waxing brings opportunities for reflection and growth. (Moon: 78.3% illuminated)

💕 Compatibility Example:
   Cancer (Water) and Pisces (Water)
   Score: 85/100
   Highly Compatible

==================================================
Follow @moonstruckimmemorial for more astrology insights!
```

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Inspiration

This project is inspired by the cosmic wisdom shared by [@moonstruckimmemorial](https://www.tiktok.com/@moonstruckimmemorial) on TikTok.

## License

Open source - feel free to use and modify as needed.

---

✨ *May the stars guide your path* ✨