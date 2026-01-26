#!/usr/bin/env python3
"""
MoonStruck Astrology - Usage Examples

This file demonstrates various use cases of the MoonStruck Astrology module.
Inspired by @moonstruckimmemorial
"""

from moonstruck_astrology import MoonStruckAstrology
import datetime


def example_basic_usage():
    """Basic usage example."""
    print("=" * 60)
    print("EXAMPLE 1: Basic Usage")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Get your zodiac sign
    my_birthday = datetime.date(1995, 8, 15)
    my_sign = astrology.get_zodiac_sign(my_birthday)
    print(f"\n🎂 Birthday: {my_birthday.strftime('%B %d, %Y')}")
    print(f"♈︎ Zodiac Sign: {my_sign}")
    
    # Get detailed info
    info = astrology.get_zodiac_info(my_sign)
    print(f"\n✨ {my_sign} Details:")
    print(f"   Symbol: {info['symbol']}")
    print(f"   Element: {info['element']}")
    print(f"   Ruling Planet: {info['ruling_planet']}")
    print(f"   Traits: {', '.join(info['traits'])}")


def example_moon_tracking():
    """Moon phase tracking example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Moon Phase Tracking")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Current moon phase
    moon_phase, illumination = astrology.get_moon_phase()
    print(f"\n🌙 Current Moon Phase: {moon_phase}")
    print(f"💫 Illumination: {illumination}%")
    
    # Check moon phase for the next week
    print("\n📅 Moon Phases for Next 7 Days:")
    today = datetime.datetime.now()
    for i in range(7):
        date = today + datetime.timedelta(days=i)
        phase, illum = astrology.get_moon_phase(date)
        print(f"   {date.strftime('%b %d')}: {phase} ({illum}%)")


def example_compatibility():
    """Compatibility checking example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Zodiac Compatibility")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Check compatibility between different signs
    pairs = [
        ("Cancer", "Pisces"),
        ("Aries", "Leo"),
        ("Taurus", "Virgo"),
        ("Gemini", "Libra"),
    ]
    
    print("\n💕 Compatibility Readings:")
    for sign1, sign2 in pairs:
        compat = astrology.get_compatibility(sign1, sign2)
        print(f"\n   {compat['sign1']} + {compat['sign2']}")
        print(f"   Score: {compat['score']}/100")
        print(f"   Status: {compat['compatibility']}")


def example_daily_insights():
    """Daily insights example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Daily Astrological Insights")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Get insights for different signs
    featured_signs = ["Aries", "Cancer", "Libra", "Capricorn"]
    
    print("\n🔮 Today's Insights:")
    for sign in featured_signs:
        insight = astrology.get_daily_insight(sign)
        print(f"\n   {insight}")


def example_birth_chart():
    """Birth chart example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Birth Chart Summary")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Generate birth chart
    birth_date = datetime.date(1992, 12, 5)
    chart = astrology.get_birth_chart_summary(birth_date)
    
    print(f"\n📊 Birth Chart for {chart['birth_date']}:")
    print(f"   {chart['symbol']} Sun Sign: {chart['sun_sign']}")
    print(f"   🔥 Element: {chart['element']}")
    print(f"   🪐 Ruling Planet: {chart['ruling_planet']}")
    print(f"   ✨ Key Traits:")
    for trait in chart['traits']:
        print(f"      • {trait.capitalize()}")


def example_all_zodiac_signs():
    """Display all zodiac signs."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: All Zodiac Signs Reference")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    print("\n🌟 Complete Zodiac Guide:\n")
    for sign, start, end in astrology.ZODIAC_SIGNS:
        info = astrology.get_zodiac_info(sign)
        start_str = f"{start[0]}/{start[1]}"
        end_str = f"{end[0]}/{end[1]}"
        
        print(f"{info['symbol']} {sign:12} ({start_str} - {end_str})")
        print(f"   Element: {info['element']:6} | Planet: {info['ruling_planet']}")
        print()


def example_relationship_analysis():
    """Detailed relationship analysis example."""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Relationship Analysis")
    print("=" * 60)
    
    astrology = MoonStruckAstrology()
    
    # Analyze a specific relationship
    person1_birthday = datetime.date(1990, 7, 15)  # Cancer
    person2_birthday = datetime.date(1992, 11, 8)  # Scorpio
    
    sign1 = astrology.get_zodiac_sign(person1_birthday)
    sign2 = astrology.get_zodiac_sign(person2_birthday)
    
    print(f"\n💑 Relationship Analysis:")
    print(f"   Person 1: {sign1} (born {person1_birthday.strftime('%B %d, %Y')})")
    print(f"   Person 2: {sign2} (born {person2_birthday.strftime('%B %d, %Y')})")
    
    info1 = astrology.get_zodiac_info(sign1)
    info2 = astrology.get_zodiac_info(sign2)
    
    print(f"\n   {sign1} ({info1['element']}) Traits:")
    print(f"   {', '.join(info1['traits'][:3])}")
    
    print(f"\n   {sign2} ({info2['element']}) Traits:")
    print(f"   {', '.join(info2['traits'][:3])}")
    
    compatibility = astrology.get_compatibility(sign1, sign2)
    print(f"\n   💕 Compatibility Score: {compatibility['score']}/100")
    print(f"   Status: {compatibility['compatibility']}")


def main():
    """Run all examples."""
    print("\n✨ MoonStruck Astrology - Complete Examples ✨")
    print("Inspired by @moonstruckimmemorial\n")
    
    example_basic_usage()
    example_moon_tracking()
    example_compatibility()
    example_daily_insights()
    example_birth_chart()
    example_all_zodiac_signs()
    example_relationship_analysis()
    
    print("\n" + "=" * 60)
    print("🌙 Follow @moonstruckimmemorial for more cosmic wisdom! 🌙")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
