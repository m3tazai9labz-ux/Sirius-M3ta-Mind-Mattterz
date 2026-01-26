#!/usr/bin/env python3
"""
Test suite for MoonStruck Astrology Module

Tests for zodiac sign calculations, moon phases, compatibility,
and other astrological features.
"""

import unittest
import datetime
from moonstruck_astrology import MoonStruckAstrology


class TestMoonStruckAstrology(unittest.TestCase):
    """Test cases for MoonStruck Astrology functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.astrology = MoonStruckAstrology()
    
    def test_zodiac_sign_determination(self):
        """Test zodiac sign calculation for various dates."""
        test_cases = [
            (datetime.date(1990, 3, 25), "Aries"),
            (datetime.date(1990, 4, 25), "Taurus"),
            (datetime.date(1990, 5, 25), "Gemini"),
            (datetime.date(1990, 6, 25), "Cancer"),
            (datetime.date(1990, 7, 25), "Leo"),
            (datetime.date(1990, 8, 25), "Virgo"),
            (datetime.date(1990, 9, 25), "Libra"),
            (datetime.date(1990, 10, 25), "Scorpio"),
            (datetime.date(1990, 11, 25), "Sagittarius"),
            (datetime.date(1990, 12, 25), "Capricorn"),
            (datetime.date(1990, 1, 25), "Aquarius"),
            (datetime.date(1990, 2, 25), "Pisces"),
        ]
        
        for birth_date, expected_sign in test_cases:
            with self.subTest(date=birth_date):
                result = self.astrology.get_zodiac_sign(birth_date)
                self.assertEqual(result, expected_sign)
    
    def test_zodiac_boundary_dates(self):
        """Test zodiac sign determination at boundary dates."""
        # Test first day of Aries
        self.assertEqual(
            self.astrology.get_zodiac_sign(datetime.date(2000, 3, 21)),
            "Aries"
        )
        # Test last day of Aries
        self.assertEqual(
            self.astrology.get_zodiac_sign(datetime.date(2000, 4, 19)),
            "Aries"
        )
        # Test first day of Taurus
        self.assertEqual(
            self.astrology.get_zodiac_sign(datetime.date(2000, 4, 20)),
            "Taurus"
        )
    
    def test_moon_phase_calculation(self):
        """Test moon phase calculation returns valid data."""
        phase_name, illumination = self.astrology.get_moon_phase()
        
        # Check that phase name is one of the valid phases
        valid_phases = [
            "New Moon 🌑", "Waxing Crescent 🌒", "First Quarter 🌓",
            "Waxing Gibbous 🌔", "Full Moon 🌕", "Waning Gibbous 🌖",
            "Last Quarter 🌗", "Waning Crescent 🌘"
        ]
        self.assertIn(phase_name, valid_phases)
        
        # Check illumination is within valid range
        self.assertGreaterEqual(illumination, 0.0)
        self.assertLessEqual(illumination, 100.0)
    
    def test_moon_phase_with_specific_date(self):
        """Test moon phase calculation with a specific date."""
        # Test with known new moon date
        test_date = datetime.datetime(2000, 1, 6, 18, 14)
        phase_name, illumination = self.astrology.get_moon_phase(test_date)
        
        # Should be close to new moon
        self.assertIn("New Moon", phase_name)
        self.assertLess(illumination, 10.0)  # Very low illumination
    
    def test_zodiac_info_exists(self):
        """Test that zodiac info is available for all signs."""
        for sign, _, _ in self.astrology.ZODIAC_SIGNS:
            with self.subTest(sign=sign):
                info = self.astrology.get_zodiac_info(sign)
                
                # Check all required fields exist
                self.assertIn("element", info)
                self.assertIn("ruling_planet", info)
                self.assertIn("traits", info)
                self.assertIn("symbol", info)
                
                # Check element is valid
                self.assertIn(info["element"], ["Fire", "Earth", "Air", "Water"])
                
                # Check traits is a list
                self.assertIsInstance(info["traits"], list)
                self.assertGreater(len(info["traits"]), 0)
    
    def test_compatibility_calculation(self):
        """Test compatibility calculation between signs."""
        # Test compatible elements (Water with Water)
        compatibility = self.astrology.get_compatibility("Cancer", "Pisces")
        self.assertEqual(compatibility["sign1"], "Cancer")
        self.assertEqual(compatibility["sign2"], "Pisces")
        self.assertIsInstance(compatibility["score"], int)
        self.assertGreaterEqual(compatibility["score"], 0)
        self.assertLessEqual(compatibility["score"], 100)
        
        # Test same element compatibility
        self.assertGreater(compatibility["score"], 60)
    
    def test_compatibility_all_signs(self):
        """Test compatibility calculation works for all sign combinations."""
        signs = [sign for sign, _, _ in self.astrology.ZODIAC_SIGNS]
        
        for sign1 in signs[:3]:  # Test a few combinations
            for sign2 in signs[:3]:
                with self.subTest(sign1=sign1, sign2=sign2):
                    compatibility = self.astrology.get_compatibility(sign1, sign2)
                    self.assertIn("score", compatibility)
                    self.assertIn("compatibility", compatibility)
    
    def test_daily_insight_generation(self):
        """Test daily insight generation."""
        sign = "Leo"
        insight = self.astrology.get_daily_insight(sign)
        
        # Check insight is a string
        self.assertIsInstance(insight, str)
        
        # Check insight contains the sign
        self.assertIn(sign, insight)
        
        # Check insight is not empty
        self.assertGreater(len(insight), 20)
    
    def test_daily_insight_deterministic(self):
        """Test that daily insight is deterministic for the same date."""
        sign = "Virgo"
        test_date = datetime.date(2023, 6, 15)
        
        insight1 = self.astrology.get_daily_insight(sign, test_date)
        insight2 = self.astrology.get_daily_insight(sign, test_date)
        
        # Same date should produce same insight
        self.assertEqual(insight1, insight2)
    
    def test_birth_chart_summary(self):
        """Test birth chart summary generation."""
        birth_date = datetime.date(1990, 7, 15)
        chart = self.astrology.get_birth_chart_summary(birth_date)
        
        # Check all required fields
        self.assertIn("sun_sign", chart)
        self.assertIn("element", chart)
        self.assertIn("ruling_planet", chart)
        self.assertIn("traits", chart)
        self.assertIn("symbol", chart)
        self.assertIn("birth_date", chart)
        
        # Verify sun sign matches zodiac sign
        expected_sign = self.astrology.get_zodiac_sign(birth_date)
        self.assertEqual(chart["sun_sign"], expected_sign)
        
        # Verify traits is a list
        self.assertIsInstance(chart["traits"], list)
    
    def test_all_zodiac_elements(self):
        """Test that all four elements are represented."""
        elements = set()
        for sign, _, _ in self.astrology.ZODIAC_SIGNS:
            info = self.astrology.get_zodiac_info(sign)
            elements.add(info["element"])
        
        expected_elements = {"Fire", "Earth", "Air", "Water"}
        self.assertEqual(elements, expected_elements)
    
    def test_zodiac_sign_count(self):
        """Test that all 12 zodiac signs are present."""
        self.assertEqual(len(self.astrology.ZODIAC_SIGNS), 12)
        self.assertEqual(len(self.astrology.ZODIAC_TRAITS), 12)


class TestMoonPhaseAccuracy(unittest.TestCase):
    """Additional tests for moon phase calculation accuracy."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.astrology = MoonStruckAstrology()
    
    def test_full_moon_illumination(self):
        """Test that full moon has high illumination."""
        # Calculate approximate full moon (14.765 days after new moon)
        days_to_full = 14.765
        full_moon_date = self.astrology.known_new_moon + datetime.timedelta(days=days_to_full)
        
        phase_name, illumination = self.astrology.get_moon_phase(full_moon_date)
        
        # Full moon should have illumination close to 100%
        self.assertGreater(illumination, 95.0)
        self.assertIn("Full", phase_name)
    
    def test_lunar_cycle_consistency(self):
        """Test that lunar cycle returns to same phase after full cycle."""
        start_date = datetime.datetime(2023, 1, 1)
        
        phase1, illum1 = self.astrology.get_moon_phase(start_date)
        
        # Move forward one complete lunar cycle
        end_date = start_date + datetime.timedelta(days=self.astrology.lunar_month)
        phase2, illum2 = self.astrology.get_moon_phase(end_date)
        
        # Phases should be similar (within 10% illumination)
        self.assertAlmostEqual(illum1, illum2, delta=10.0)


if __name__ == "__main__":
    unittest.main()
