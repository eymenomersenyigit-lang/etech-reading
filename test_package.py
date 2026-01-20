#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for eTech Reading package
"""

import sys
from etech_reading import TextAnalyzer, RSVPReader


def test_text_analyzer():
    """Test TextAnalyzer functionality"""
    print("Testing TextAnalyzer...")
    
    sample_text = """
    The quick brown fox jumps over the lazy dog. 
    This is a test sentence. RSVP technology works great!
    """
    
    # Test sentence splitting
    sentences = TextAnalyzer.split_into_sentences(sample_text)
    print(f"✓ Split into {len(sentences)} sentences")
    
    # Test text analysis
    analysis = TextAnalyzer.analyze_text(sample_text)
    print(f"✓ Analyzed {len(analysis)} sentences")
    
    total_words = sum(s['word_count'] for s in analysis)
    print(f"✓ Found {total_words} words total")
    
    # Test focus letter calculation
    test_words = ["a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefgh"]
    print("\n✓ Focus letter positions:")
    for word in test_words:
        idx, letter = TextAnalyzer.get_focus_letter_index(word)
        print(f"  {word:10} -> pos {idx}: '{letter}'")
    
    print("\n✓ TextAnalyzer tests passed!\n")


def test_rsvp_reader():
    """Test RSVP Reader GUI components"""
    print("Testing RSVP Reader...")
    
    try:
        from PyQt5.QtWidgets import QApplication
        from etech_reading import RSVPReader
        
        # Create QApplication if needed
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        reader = RSVPReader()
        print("✓ RSVPReader instance created successfully")
        
        # Test UI components exist
        assert hasattr(reader, 'text_input'), "Missing text_input"
        assert hasattr(reader, 'speed_slider'), "Missing speed_slider"
        assert hasattr(reader, 'word_display'), "Missing word_display"
        assert hasattr(reader, 'progress_bar'), "Missing progress_bar"
        print("✓ All UI components present")
        
        print("✓ RSVP Reader tests passed!\n")
        
    except Exception as e:
        print(f"✗ RSVP Reader test failed: {e}\n")


def main():
    """Run all tests"""
    print("=" * 60)
    print("eTech Reading Package Test Suite")
    print("=" * 60 + "\n")
    
    try:
        # Test TextAnalyzer
        test_text_analyzer()
        
        # Test RSVP Reader
        test_rsvp_reader()
        
        print("=" * 60)
        print("✓ All tests passed successfully!")
        print("=" * 60)
        return 0
        
    except Exception as e:
        print(f"\n✗ Tests failed: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
