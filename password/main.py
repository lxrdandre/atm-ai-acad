"""
Password Strength Validator Challenge
A comprehensive password security checker that evaluates passwords,
detects weak patterns, and provides meaningful feedback to users.

This is a skeleton file. Implement the functions according to their docstrings.
"""

import re
import os


# Load common passwords from the file
def load_common_passwords():
    """Load the list of common passwords from the NCSC file."""
    # TODO: Read from the 100k-most-used-passwords-NCSC.txt file
    file_path = os.path.join(os.path.dirname(__file__), "100k-most-used-passwords-NCSC.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        common_passwords = set(line.strip().lower() for line in f)
    # TODO: Return a set of lowercase passwords for fast lookup
    return common_passwords


COMMON_PASSWORDS = load_common_passwords()


def check_length(password):
    """
    Check whether the password meets the minimum length rule.
    
    Analytical questions:
    - What is a reasonable minimum length? (Hint: 8 is industry standard)
    - Should length alone be enough to pass?
    - How do you phrase feedback that is helpful but not preachy?
    
    Args:
        password (str): The password to check
        
    Returns:
        dict: Must contain:
            - 'valid' (bool): True if length is acceptable (>= 8 chars)
            - 'feedback' (str): Clear message about the length assessment
            - 'length' (int): The actual length of the password
            - 'meets_minimum' (bool): True if >= 8 characters
    
    Examples:
        >>> result = check_length("short")
        >>> result['valid']
        False
        >>> result['meets_minimum']
        False
    """
    # TODO: Determine password length
    length = len(password)
    # TODO: Check if it meets minimum of 8 characters
    meets_minimum = length >= 8
    # TODO: Return appropriate feedback
    return {
        'valid': meets_minimum,
        'feedback': f"Password is {length} characters long." if meets_minimum else f"Password is only {length} characters long. It should be at least 8 characters.",
        'length': length,
        'meets_minimum': meets_minimum
    }


def check_character_types(password):
    """
    Inspect the character variety inside the password.
    
    Security thinking:
    - Why does character variety matter? (Hint: It increases the search space for attackers)
    - Is 4 different types required? Or is 3 enough?
    - How do you give the user helpful feedback about what they're missing?
    
    Args:
        password (str): The password to check
        
    Returns:
        dict: Must contain:
            - 'valid' (bool): True if at least 3 different character types present
            - 'has_lowercase' (bool): True if contains a-z
            - 'has_uppercase' (bool): True if contains A-Z
            - 'has_digits' (bool): True if contains 0-9
            - 'has_special' (bool): True if contains !@#$%^&*() etc.
            - 'character_variety_score' (int): Count of how many types present (0-4)
            - 'missing' (list): List of missing character types (e.g., ['digits', 'special characters'])
            - 'feedback' (str): Summary of character types and what's missing
    
    Examples:
        >>> result = check_character_types("password")
        >>> result['has_digits']
        False
        >>> result['character_variety_score']
        1
    """
    # TODO: Check for lowercase letters using regex or built-in methods
    has_lowercase = any(c.islower() for c in password)
    # TODO: Check for uppercase letters
    has_uppercase = any(c.isupper() for c in password)
    # TODO: Check for digits
    has_digits = any(c.isdigit() for c in password)
    # TODO: Check for special characters (!@#$%^&*()_+-=[]{};:\'",.<>?/\\|`~)
    has_special = any(not c.isalnum() for c in password)
    # TODO: Count variety (0-4)
    character_variety_score = sum([has_lowercase, has_uppercase, has_digits, has_special])
    # TODO: Build list of missing types
    missing = []
    if not has_lowercase:
        missing.append("lowercase letters")
    if not has_uppercase:
        missing.append("uppercase letters")
    if not has_digits:
        missing.append("digits")
    if not has_special:
        missing.append("special characters")
    # TODO: Generate helpful feedback
    feedback = f"Character variety: {character_variety_score}/4"
    if missing:
        feedback += f". Missing: {', '.join(missing)}."
    return {
        'valid': character_variety_score >= 3,
        'has_lowercase': has_lowercase,
        'has_uppercase': has_uppercase,
        'has_digits': has_digits,
        'has_special': has_special,
        'character_variety_score': character_variety_score,
        'missing': missing,
        'feedback': feedback
    }


def contains_common_password(password):
    """
    Check whether the password is too common.
    
    Real-world security thinking:
    - Why should users avoid commonly used passwords? (Hint: Attackers have lists of millions)
    - Should the comparison be case-sensitive or case-insensitive? Why?
    - How severe is this issue compared to other checks?
    
    Args:
        password (str): The password to check
        
    Returns:
        dict: Must contain:
            - 'is_common' (bool): True if password found in COMMON_PASSWORDS set
            - 'feedback' (str): Warning if common, encouraging message if not
    
    Examples:
        >>> result = contains_common_password("password123")
        >>> result['is_common']
        True
    """
    # TODO: Convert password to lowercase for case-insensitive comparison
    password_lower = password.lower()
    # TODO: Check if it exists in COMMON_PASSWORDS set
    is_common = password_lower in COMMON_PASSWORDS
    # TODO: Return result with appropriate warning if found
    return {
        'is_common': is_common,
        'feedback': "This password is commonly used and may be easy to guess." if is_common else "This password is not commonly used."
    }


def contains_personal_info(password, username=None):
    """
    Check whether the password includes obvious personal information.
    
    Maintainability thinking:
    - What if you later need to check email addresses or full names too?
    - How can you make this function extensible?
    
    Args:
        password (str): The password to check
        username (str, optional): The username to check for in password
        
    Returns:
        dict: Must contain:
            - 'contains_personal_info' (bool): True if personal info detected
            - 'found_patterns' (list): List of found patterns (e.g., ["Username 'john' found in password"])
            - 'feedback' (str): Warning or positive message
    
    Hints:
        - Check if username appears anywhere in password (case-insensitive)
        - Check if first few characters of username appear
        - Look for reversed username
    
    Examples:
        >>> result = contains_personal_info("john2024", "john")
        >>> result['contains_personal_info']
        True
    """
    # TODO: Handle case where username is None (return early with neutral result)
    if username is not None:
        username = username.strip()

    if not username:
        return {
            'contains_personal_info': False,
            'found_patterns': [],
            'feedback': "No username provided for personal info check."
        }
    # TODO: Convert both password and username to lowercase for comparison
    password_lower = password.lower()
    username_lower = username.lower()
    # TODO: Check if username appears directly in password
    found_patterns = []
    if username_lower in password_lower:
        found_patterns.append(f"Username '{username}' found in password")
    # TODO: Check for partial matches (first N characters)
    elif len(username_lower) >= 3 and username_lower[:3] in password_lower:
        found_patterns.append(f"First 3 characters of username '{username[:3]}' found in password")
    reversed_username = username_lower[::-1]
    if len(username_lower) >= 3 and reversed_username != username_lower and reversed_username in password_lower:
        found_patterns.append(f"Reversed username '{username[::-1]}' found in password")
    # TODO: Build list of patterns found
    contains_personal_info = len(found_patterns) > 0
    # TODO: Generate appropriate feedback
    return {
        'contains_personal_info': contains_personal_info,
        'found_patterns': found_patterns,
        'feedback': "Personal information found in password." if contains_personal_info else "No obvious personal information found."
    }


def has_repeated_or_sequential_patterns(password):
    """
    Detect patterns that make the password weak.
    
    Pattern detection thinking:
    - What makes a pattern "obvious to attackers"?
    - Which patterns are easiest to guess? (Hint: 123, abc, qwerty)
    - How do you balance catching real patterns without false positives?
    
    Args:
        password (str): The password to check
        
    Returns:
        dict: Must contain:
            - 'has_patterns' (bool): True if any weak patterns detected
            - 'patterns_found' (list): List of pattern descriptions found
            - 'severity' (str): 'none', 'low', 'medium', or 'high'
            - 'feedback' (str): Explanation of patterns and why they're weak
    
    Patterns to detect:
        - Repeated characters: aaa, 111, !!! (3+ in a row)
        - Sequential digits: 123, 234, 456, 789
        - Sequential letters: abc, def, xyz (case-insensitive)
        - Keyboard patterns: qwerty, asdfgh, 1qaz, qazwsx
        - Repeated chunks: if 'ab' appears multiple times separately
    
    Examples:
        >>> result = has_repeated_or_sequential_patterns("aaa111bbb")
        >>> result['has_patterns']
        True
        >>> len(result['patterns_found']) > 0
        True
    """
    # TODO: Check for 3+ repeated characters using regex (.)\1{2,}
    repeated_char_pattern = re.compile(r"(.)\1{2,}")
    repeated_char_matches = repeated_char_pattern.findall(password)
    patterns_found = []
    if repeated_char_matches:
        patterns_found.append(f"Repeated character '{repeated_char_matches[0]}' found 3 or more times in a row")
    # TODO: Check for sequential digits (012, 123, 234, ..., 890)
    sequential_digits_pattern = re.compile(r"012|123|234|345|456|567|678|789")
    if sequential_digits_pattern.search(password):
        patterns_found.append("Sequential digits found (e.g., 123, 234)")
    # TODO: Check for sequential letters (abc, bcd, ..., xyz)
    sequential_letters_pattern = re.compile(r"abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz", re.IGNORECASE)
    if sequential_letters_pattern.search(password):
        patterns_found.append("Sequential letters found (e.g., abc, def)")
    # TODO: Check for common keyboard patterns (qwerty, asdfgh, zxcvbn, qazwsx)
    keyboard_patterns = ["qwerty", "asdfgh", "zxcvbn", "1qaz", "qazwsx"]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            patterns_found.append(f"Keyboard pattern '{pattern}' found in password")
    # TODO: Check for repeated chunks (substring appears more than once)
    chunk_pattern = re.compile(r"(\w{2,})\w*\1")
    chunk_matches = chunk_pattern.findall(password)
    if chunk_matches:
        patterns_found.append(f"Repeated chunk '{chunk_matches[0]}' found in password")
    # TODO: Determine severity based on what was found
    if not patterns_found:
        severity = 'none'
    elif len(patterns_found) == 1:
        severity = 'low'
    elif len(patterns_found) == 2:
        severity = 'medium'
    else:
        severity = 'high'
    # TODO: Build clear feedback message
    feedback = "Weak patterns detected: " + "; ".join(patterns_found) if patterns_found else "No obvious weak patterns found."
    return {
        'has_patterns': len(patterns_found) > 0,
        'patterns_found': patterns_found,
        'severity': severity,
        'feedback': feedback
    }


def calculate_strength(password, username=None):
    """
    Estimate the overall strength of the password by combining all checks.
    
    Scoring strategy:
    - What should each check be worth? (Hint: Length is foundational, patterns are dealbreakers)
    - How do you weight different issues?
    - Should a common password completely tank the score?
    
    Args:
        password (str): The password to check
        username (str, optional): The username for personal info check
        
    Returns:
        dict: Must contain:
            - 'score' (int): Numeric score from 0-100
            - 'strength' (str): One of 'very_weak', 'weak', 'medium', 'strong'
            - 'reasoning' (list): List of strings explaining the score
            - 'checks' (dict): Results from all other check functions
    
    Scoring suggestion:
        - Start with 0
        - Length >= 8: +15, >= 12: +18, >= 16: +20
        - Each character type: +7 (0-28 total)
        - Common password: -50
        - Personal info: -20
        - Has patterns: -15
        - Clamp result to 0-100
    
    Strength levels:
        - 80+: strong
        - 60-79: medium
        - 40-59: weak
        - 0-39: very_weak
    
    Examples:
        >>> result = calculate_strength("MyP@ssw0rd!", "john")
        >>> result['score'] >= 70
        True
        >>> result['strength']
        'strong'
    """
    # TODO: Call all check functions with the password and username
    length_check = check_length(password)
    character_check = check_character_types(password)
    common_password_check = contains_common_password(password)
    personal_info_check = contains_personal_info(password, username)
    patterns_check = has_repeated_or_sequential_patterns(password)

    # TODO: Collect all results in a checks dict
    checks = {
        'length': length_check,
        'character_variety': character_check,
        'common_password': common_password_check,
        'personal_info': personal_info_check,
        'patterns': patterns_check
    }

    # TODO: Initialize score to 0
    positive_score = 0

    # TODO: Add points for length
    if length_check['valid']:
        positive_score += 15
        if length_check['length'] >= 12:
            positive_score += 3
        if length_check['length'] >= 16:
            positive_score += 2

    # TODO: Add points for character variety
    positive_score += character_check['character_variety_score'] * 7

    max_positive_score = 48
    score = round((positive_score / max_positive_score) * 100)

    # TODO: Deduct points for common password (critical!)
    if common_password_check['is_common']:
        score -= 50
    # TODO: Deduct points for personal info
    if personal_info_check['contains_personal_info']:
        score -= 20
    # TODO: Deduct points for patterns
    if patterns_check['has_patterns']:
        score -= 15
    # TODO: Clamp score to 0-100 range
    score = max(0, min(100, score))
    # TODO: Determine strength level based on score
    if score >= 80:
        strength = 'strong'
    elif score >= 60:
        strength = 'medium'
    elif score >= 40:
        strength = 'weak'
    else:
        strength = 'very_weak'
    # TODO: Build reasoning list with both positives and negatives
    reasoning = _build_strength_reasoning(checks, score, strength)
    return {
        'score': score,
        'strength': strength,
        'reasoning': reasoning,
        'checks': checks
    }




def validate_password(password, username=None):
    """
    Build the final validator that applies all important checks.
    
    Design thinking:
    - Which checks are mandatory failures vs warnings?
    - How do you structure feedback so another system can use it?
    - What would an API endpoint need from this function?
    
    Args:
        password (str): The password to validate
        username (str, optional): The username for personal info check
        
    Returns:
        dict: Structured validation result containing:
            - 'is_valid' (bool): True if password passes all critical checks
            - 'strength_level' (str): 'very_weak', 'weak', 'medium', or 'strong'
            - 'strength_score' (int): 0-100 score
            - 'errors' (list): Critical issues that prevent password acceptance
            - 'warnings' (list): Issues that should alert user but may not block submission
            - 'requirements_met' (list): List of met requirements
            - 'requirements_missing' (list): List of unmet requirements
            - 'feedback_summary' (list): Detailed reasoning
            - 'detailed_checks' (dict): Results from each individual check
    
    Critical errors (password rejected):
        - Too short (< 8 chars)
        - Is a common password
        - Insufficient character variety (< 3 types)
    
    Warnings (password accepted but flagged):
        - Contains personal info
        - Has weak patterns
        - Weak character variety (2 types)
    
    Examples:
        >>> result = validate_password("weak", "john")
        >>> result['is_valid']
        False
        >>> len(result['errors']) > 0
        True
    """
    # TODO: Call calculate_strength to get overall assessment
    strength_result = calculate_strength(password, username)
    # TODO: Collect all check results
    strength_checks = strength_result['checks']
    checks = {
        'length': strength_checks['length'],
        'characters': strength_checks['character_variety'],
        'common_password': strength_checks['common_password'],
        'personal_info': strength_checks['personal_info'],
        'patterns': strength_checks['patterns']
    }
    # TODO: Build errors list for critical issues
    errors = []
    if not checks['length']['meets_minimum']:
        errors.append("Password is too short (less than 8 characters).")
    if checks['common_password']['is_common']:
        errors.append("Password is too common and may be easily guessed.")
    if checks['characters']['character_variety_score'] < 3:
        errors.append("Password lacks sufficient character variety (needs at least 3 types).")
    # TODO: Build warnings list for advisory issues
    warnings = []
    if checks['personal_info']['contains_personal_info']:
        warnings.append("Password contains personal information which may be easy to guess.")
    if checks['patterns']['has_patterns']:
        warnings.append("Password contains weak patterns that may be easily guessed.")
    if checks['characters']['character_variety_score'] == 2:
        warnings.append("Password has weak character variety (only 2 types).")
    # TODO: Compile requirements_met list
    requirements_met = []
    if checks['length']['meets_minimum']:
        requirements_met.append("Minimum length (8+ characters)")
    if checks['characters']['character_variety_score'] >= 3:
        requirements_met.append("Sufficient character variety (3+ types)")
    if not checks['common_password']['is_common']:
        requirements_met.append("Not a common password")
    # TODO: Compile requirements_missing list
    requirements_missing = []
    if not checks['length']['meets_minimum']:
        requirements_missing.append("Minimum length (8+ characters)")
    if checks['characters']['character_variety_score'] < 3:
        requirements_missing.append("Sufficient character variety (3+ types)")
    if checks['common_password']['is_common']:
        requirements_missing.append("Not a common password")
    # TODO: Determine is_valid (no critical errors)
    is_valid = len(errors) == 0
    # TODO: Return comprehensive dict with all fields
    return {
        'is_valid': is_valid,
        'strength_level': strength_result['strength'],
        'strength_score': strength_result['score'],
        'errors': errors,
        'warnings': warnings,
        'requirements_met': requirements_met,
        'requirements_missing': requirements_missing,
        'feedback_summary': strength_result['reasoning'],
        'detailed_checks': checks
    }


# HELPER FUNCTIONS (Optional)

def _build_strength_reasoning(checks, score, strength):
    """Helper function to build detailed reasoning for strength assessment."""
    # TODO: Create list of positive findings
    positive_findings = []
    # TODO: Create list of negative findings
    negative_findings = []

    length_check = checks['length']
    character_check = checks['character_variety']
    common_password_check = checks['common_password']
    personal_info_check = checks['personal_info']
    patterns_check = checks['patterns']

    positive_findings.append(f"Overall strength: {strength.replace('_', ' ')} ({score}/100).")

    if length_check['meets_minimum']:
        positive_findings.append(length_check['feedback'])
    else:
        negative_findings.append(length_check['feedback'])

    if character_check['valid']:
        positive_findings.append(character_check['feedback'])
    else:
        negative_findings.append(character_check['feedback'])

    if common_password_check['is_common']:
        negative_findings.append(common_password_check['feedback'])
    else:
        positive_findings.append(common_password_check['feedback'])

    if personal_info_check['contains_personal_info']:
        negative_findings.append(personal_info_check['feedback'])
        negative_findings.extend(personal_info_check['found_patterns'])
    else:
        positive_findings.append(personal_info_check['feedback'])

    if patterns_check['has_patterns']:
        negative_findings.append(patterns_check['feedback'])
    else:
        positive_findings.append(patterns_check['feedback'])

    # TODO: Format as human-readable feedback
    return positive_findings + negative_findings


def print_validation_result(password, username=None):
    """Pretty print validation results for testing."""
    # TODO: Format and display validation results nicely
    result = validate_password(password, username)

    print("=" * 70)
    print(f"Password: {password}")
    if username:
        print(f"Username: {username}")
    print(f"Valid: {'Yes' if result['is_valid'] else 'No'}")
    print(f"Strength: {result['strength_level'].replace('_', ' ').title()} ({result['strength_score']}/100)")

    # TODO: Show errors, warnings, requirements, and reasoning
    if result['errors']:
        print("\nErrors:")
        for error in result['errors']:
            print(f"  - {error}")

    if result['warnings']:
        print("\nWarnings:")
        for warning in result['warnings']:
            print(f"  - {warning}")

    if result['requirements_met']:
        print("\nRequirements met:")
        for requirement in result['requirements_met']:
            print(f"  - {requirement}")

    if result['requirements_missing']:
        print("\nRequirements missing:")
        for requirement in result['requirements_missing']:
            print(f"  - {requirement}")

    if result['feedback_summary']:
        print("\nReasoning:")
        for item in result['feedback_summary']:
            print(f"  - {item}")


# TEST SECTION

if __name__ == "__main__":
    print("\nPASSWORD STRENGTH VALIDATOR - Test Suite")
    print("Testing with various password examples\n")
    
    test_cases = [
        # ("short", None, "Very short password"),
        # ("lowercase", None, "Only lowercase letters"),
        # ("12345678", None, "Only numbers"),
        # ("Password1", None, "Uppercase, lowercase, digits, but no special chars"),
        # ("password", None, "Common password"),
        # ("john123", "john", "Contains username"),
        # ("aaaaaa123", None, "Repeated characters"),
        # ("abc123def", None, "Sequential pattern"),
        # ("Str0ng!Pass", None, "Good variety, no patterns"),
        # ("MyP@ssw0rd!", None, "Strong password with special char"),
        # ("P@ssw0rd!2024Secure#", None, "Very strong password"),
        ("abcfish223", None, "test"),
    ]
    
    for password, username, description in test_cases:
        print(f"\nTEST: {description}")
        print_validation_result(password, username)
    
    print("\n" + "="*70)
    print("Test suite complete!")
    print("="*70)
