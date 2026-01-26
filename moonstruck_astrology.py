#!/usr/bin/env python3
"""
MoonStruck Astrology Module

A comprehensive astrology module for calculating moon phases, zodiac signs,
and astrological insights. Inspired by @moonstruckimmemorial.

This module provides:
- Moon phase calculations
- Zodiac sign determination
- Daily astrological insights
- Compatibility readings
"""

import datetime
import math
from typing import Dict, List, Tuple


class MoonStruckAstrology:
    """Main class for MoonStruck Astrology calculations and insights."""
    
    # Zodiac signs with their date ranges
    ZODIAC_SIGNS = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]
    
    # Zodiac traits and characteristics
    ZODIAC_TRAITS = {
        "Aries": {
            "element": "Fire",
            "ruling_planet": "Mars",
            "traits": ["passionate", "confident", "dynamic", "enthusiastic"],
            "symbol": "♈︎"
        },
        "Taurus": {
            "element": "Earth",
            "ruling_planet": "Venus",
            "traits": ["reliable", "patient", "devoted", "practical"],
            "symbol": "♉︎"
        },
        "Gemini": {
            "element": "Air",
            "ruling_planet": "Mercury",
            "traits": ["gentle", "affectionate", "curious", "adaptable"],
            "symbol": "♊︎"
        },
        "Cancer": {
            "element": "Water",
            "ruling_planet": "Moon",
            "traits": ["tenacious", "loyal", "emotional", "sympathetic"],
            "symbol": "♋︎"
        },
        "Leo": {
            "element": "Fire",
            "ruling_planet": "Sun",
            "traits": ["creative", "passionate", "generous", "cheerful"],
            "symbol": "♌︎"
        },
        "Virgo": {
            "element": "Earth",
            "ruling_planet": "Mercury",
            "traits": ["loyal", "analytical", "practical", "hardworking"],
            "symbol": "♍︎"
        },
        "Libra": {
            "element": "Air",
            "ruling_planet": "Venus",
            "traits": ["cooperative", "diplomatic", "gracious", "fair-minded"],
            "symbol": "♎︎"
        },
        "Scorpio": {
            "element": "Water",
            "ruling_planet": "Pluto",
            "traits": ["resourceful", "brave", "passionate", "stubborn"],
            "symbol": "♏︎"
        },
        "Sagittarius": {
            "element": "Fire",
            "ruling_planet": "Jupiter",
            "traits": ["generous", "idealistic", "great sense of humor"],
            "symbol": "♐︎"
        },
        "Capricorn": {
            "element": "Earth",
            "ruling_planet": "Saturn",
            "traits": ["responsible", "disciplined", "self-control", "good managers"],
            "symbol": "♑︎"
        },
        "Aquarius": {
            "element": "Air",
            "ruling_planet": "Uranus",
            "traits": ["progressive", "original", "independent", "humanitarian"],
            "symbol": "♒︎"
        },
        "Pisces": {
            "element": "Water",
            "ruling_planet": "Neptune",
            "traits": ["compassionate", "artistic", "intuitive", "gentle"],
            "symbol": "♓︎"
        }
    }
    
    def __init__(self):
        """Initialize the MoonStruck Astrology instance."""
        self.known_new_moon = datetime.datetime(2000, 1, 6, 18, 14)  # Known new moon
        self.lunar_month = 29.53058867  # Average lunar month in days
    
    def get_zodiac_sign(self, birth_date: datetime.date) -> str:
        """
        Determine the zodiac sign for a given birth date.
        
        Args:
            birth_date: The date of birth
            
        Returns:
            The zodiac sign name
        """
        month = birth_date.month
        day = birth_date.day
        
        for sign, start, end in self.ZODIAC_SIGNS:
            start_month, start_day = start
            end_month, end_day = end
            
            if start_month == end_month:
                if month == start_month and start_day <= day <= end_day:
                    return sign
            else:
                if (month == start_month and day >= start_day) or \
                   (month == end_month and day <= end_day):
                    return sign
        
        return "Unknown"
    
    def get_moon_phase(self, date: datetime.datetime = None) -> Tuple[str, float]:
        """
        Calculate the moon phase for a given date.
        
        Args:
            date: The date to calculate moon phase for (defaults to today)
            
        Returns:
            A tuple of (phase_name, illumination_percentage)
        """
        if date is None:
            date = datetime.datetime.now()
        
        # Calculate days since known new moon
        days_since_new = (date - self.known_new_moon).total_seconds() / 86400
        
        # Calculate position in lunar cycle
        phase_position = (days_since_new % self.lunar_month) / self.lunar_month
        
        # Calculate illumination percentage
        illumination = (1 - math.cos(phase_position * 2 * math.pi)) / 2 * 100
        
        # Determine phase name
        if phase_position < 0.0625 or phase_position >= 0.9375:
            phase_name = "New Moon 🌑"
        elif 0.0625 <= phase_position < 0.1875:
            phase_name = "Waxing Crescent 🌒"
        elif 0.1875 <= phase_position < 0.3125:
            phase_name = "First Quarter 🌓"
        elif 0.3125 <= phase_position < 0.4375:
            phase_name = "Waxing Gibbous 🌔"
        elif 0.4375 <= phase_position < 0.5625:
            phase_name = "Full Moon 🌕"
        elif 0.5625 <= phase_position < 0.6875:
            phase_name = "Waning Gibbous 🌖"
        elif 0.6875 <= phase_position < 0.8125:
            phase_name = "Last Quarter 🌗"
        else:
            phase_name = "Waning Crescent 🌘"
        
        return phase_name, round(illumination, 1)
    
    def get_zodiac_info(self, sign: str) -> Dict:
        """
        Get detailed information about a zodiac sign.
        
        Args:
            sign: The zodiac sign name
            
        Returns:
            A dictionary with zodiac sign information
        """
        return self.ZODIAC_TRAITS.get(sign, {})
    
    def get_compatibility(self, sign1: str, sign2: str) -> Dict:
        """
        Calculate compatibility between two zodiac signs.
        
        Args:
            sign1: First zodiac sign
            sign2: Second zodiac sign
            
        Returns:
            Compatibility information dictionary
            
        Raises:
            ValueError: If either sign is not a valid zodiac sign
        """
        # Validate inputs
        valid_signs = list(self.ZODIAC_TRAITS.keys())
        if sign1 not in valid_signs:
            raise ValueError(f"Invalid zodiac sign: {sign1}. Must be one of {', '.join(valid_signs)}")
        if sign2 not in valid_signs:
            raise ValueError(f"Invalid zodiac sign: {sign2}. Must be one of {', '.join(valid_signs)}")
        
        # Get elements for both signs
        info1 = self.ZODIAC_TRAITS.get(sign1, {})
        info2 = self.ZODIAC_TRAITS.get(sign2, {})
        
        element1 = info1.get("element", "")
        element2 = info2.get("element", "")
        
        # Simple compatibility based on elements
        compatible_elements = {
            "Fire": ["Fire", "Air"],
            "Earth": ["Earth", "Water"],
            "Air": ["Air", "Fire"],
            "Water": ["Water", "Earth"]
        }
        
        if element2 in compatible_elements.get(element1, []):
            compatibility_score = 85
            compatibility_text = "Highly Compatible"
        elif element1 == element2:
            compatibility_score = 70
            compatibility_text = "Compatible"
        else:
            compatibility_score = 45
            compatibility_text = "Challenging but Possible"
        
        return {
            "sign1": sign1,
            "sign2": sign2,
            "score": compatibility_score,
            "compatibility": compatibility_text,
            "description": f"{sign1} ({element1}) and {sign2} ({element2})"
        }
    
    def get_daily_insight(self, sign: str, date: datetime.date = None) -> str:
        """
        Generate a daily astrological insight for a zodiac sign.
        
        Args:
            sign: The zodiac sign
            date: The date for the insight (defaults to today)
            
        Returns:
            Daily insight message
            
        Raises:
            ValueError: If sign is not a valid zodiac sign
        """
        # Validate input
        valid_signs = list(self.ZODIAC_TRAITS.keys())
        if sign not in valid_signs:
            raise ValueError(f"Invalid zodiac sign: {sign}. Must be one of {', '.join(valid_signs)}")
        
        if date is None:
            date = datetime.date.today()
        
        info = self.get_zodiac_info(sign)
        moon_phase, illumination = self.get_moon_phase(datetime.datetime.combine(date, datetime.time()))
        
        insights = [
            f"Today's cosmic energy favors your {info.get('element', 'elemental')} nature.",
            f"The {moon_phase.split()[0]} brings opportunities for reflection and growth.",
            f"Your ruling planet {info.get('ruling_planet', 'the cosmos')} is in a favorable position.",
            f"Focus on your natural {', '.join(info.get('traits', ['unique'])[:2])} qualities today.",
        ]
        
        # Use date to create deterministic but varied daily insights
        day_of_year = date.timetuple().tm_yday
        selected_insight = insights[day_of_year % len(insights)]
        
        return f"{info.get('symbol', '✨')} {sign} - {selected_insight} (Moon: {illumination}% illuminated)"
    
    def get_birth_chart_summary(self, birth_date: datetime.date) -> Dict:
        """
        Get a summary birth chart for a given date.
        
        Args:
            birth_date: The birth date
            
        Returns:
            Birth chart summary dictionary
        """
        sign = self.get_zodiac_sign(birth_date)
        info = self.get_zodiac_info(sign)
        
        return {
            "sun_sign": sign,
            "element": info.get("element", "Unknown"),
            "ruling_planet": info.get("ruling_planet", "Unknown"),
            "traits": info.get("traits", []),
            "symbol": info.get("symbol", ""),
            "birth_date": birth_date.strftime("%B %d, %Y")
        }


def main():
    """Main function demonstrating MoonStruck Astrology features."""
    astrology = MoonStruckAstrology()
    
    print("✨ Welcome to MoonStruck Astrology ✨")
    print("=" * 50)
    print()
    
    # Today's moon phase
    moon_phase, illumination = astrology.get_moon_phase()
    print(f"🌙 Current Moon Phase: {moon_phase}")
    print(f"   Illumination: {illumination}%")
    print()
    
    # Example birth date
    birth_date = datetime.date(1990, 7, 15)
    sign = astrology.get_zodiac_sign(birth_date)
    
    print(f"📅 Example Birth Date: {birth_date.strftime('%B %d, %Y')}")
    print(f"♈︎ Zodiac Sign: {sign}")
    print()
    
    # Zodiac info
    info = astrology.get_zodiac_info(sign)
    print(f"🔮 {sign} Information:")
    print(f"   Element: {info.get('element', 'N/A')}")
    print(f"   Ruling Planet: {info.get('ruling_planet', 'N/A')}")
    print(f"   Traits: {', '.join(info.get('traits', []))}")
    print()
    
    # Daily insight
    insight = astrology.get_daily_insight(sign)
    print(f"💫 Daily Insight:")
    print(f"   {insight}")
    print()
    
    # Compatibility example
    compatibility = astrology.get_compatibility("Cancer", "Pisces")
    print(f"💕 Compatibility Example:")
    print(f"   {compatibility['description']}")
    print(f"   Score: {compatibility['score']}/100")
    print(f"   {compatibility['compatibility']}")
    print()
    
    print("=" * 50)
    print("Follow @moonstruckimmemorial for more astrology insights!")


if __name__ == "__main__":
    main()
