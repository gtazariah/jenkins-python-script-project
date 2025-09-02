#!/usr/bin/env python3
"""
Simple Python Script for Jenkins CI/CD Demo
"""

def main():
    """Main function that runs the script"""
    print("🚀 Jenkins CI/CD Pipeline Started!")
    print("📅 Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("✅ Script executed successfully!")
    print("📧 This output will be sent via email")
    
    # Perform some simple operations
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    print(f"🧮 Sum of numbers {numbers} is: {total}")
    
    return 0

if __name__ == "__main__":
    from datetime import datetime
    import sys
    
    try:
        sys.exit(main())
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        sys.exit(1)
