"""
Phase 0 Practice Milestone: Mini CLI Calculator & Quiz Tool
===========================================================
Concepts Practiced:
- Functions (def, parameters, return values, type hints)
- Control Flow (if / elif / else)
- Loops (while, for, break, continue)
- User input handling & validation

Author: Awolad Hossain
"""

import sys


# =====================================================================
# 1. Calculator Module
# =====================================================================

def add(a: float, b: float) -> float:
    """দুইটি সংখ্যার যোগফল নির্ণয় করে।"""
    return a + b


def subtract(a: float, b: float) -> float:
    """প্রথম সংখ্যা থেকে দ্বিতীয় সংখ্যা বিয়োগ করে।"""
    return a - b


def multiply(a: float, b: float) -> float:
    """দুইটি সংখ্যার গুণফল নির্ণয় করে।"""
    return a * b


def divide(a: float, b: float) -> float | None:
    """
    ভাগফল নির্ণয় করে। ভাজক শূন্য (0) হলে None রিটার্ন করে।
    Senior SRE Tip: ZeroDivisionError হ্যান্ডেল করা একটি ক্লাসিক প্রডাকশন প্র্যাকটিস।
    """
    if b == 0:
        print("❌ Error: শূন্য (0) দিয়ে ভাগ করা সম্ভব নয়!")
        return None
    return a / b


def power(a: float, b: float) -> float:
    """a এর পাওয়ার b (a^b) বের করে।"""
    return a ** b


def get_float_input(prompt_text: str) -> float:
    """
    ভ্যালিড ফ্লোট ইনপুট নেওয়ার জন্য হেল্পার ফাংশন।
    ইউজার ভুল ইনপুট দিলে লুপের মাধ্যমে আবার চাইবে (Input Validation Loop)।
    """
    while True:
        user_val = input(prompt_text).strip()
        try:
            return float(user_val)
        except ValueError:
            print(f"⚠️ '{user_val}' কোনো সঠিক সংখ্যা নয়! দয়া করে পুনরায় সঠিক সংখ্যা লিখুন।")


def run_calculator() -> None:
    """ক্যালকুলেটর সাব-সিস্টেম রান করার ফাংশন।"""
    print("\n" + "=" * 45)
    print("      🧮 MINI CLI CALCULATOR")
    print("=" * 45)

    while True:
        print("\nঅপারেশন নির্বাচন করুন:")
        print("  [1] যোগ (+)")
        print("  [2] বিয়োগ (-)")
        print("  [3] গুণ (*)")
        print("  [4] ভাগ (/)")
        print("  [5] পাওয়ার / ঘাত (a^b)")
        print("  [0] ক্যালকুলেটর থেকে বের হন (Back to Main Menu)")

        choice = input("\nআপনার পছন্দ লিখুন (0-5): ").strip()

        if choice == "0":
            print("👋 ক্যালকুলেটর বন্ধ হচ্ছে...")
            break

        if choice not in {"1", "2", "3", "4", "5"}:
            print("⚠️ ভুল অপশন! দয়া করে 0 থেকে 5 এর মধ্যে সিলেক্ট করুন।")
            continue

        num1 = get_float_input("প্রথম সংখ্যাটি লিখুন: ")
        num2 = get_float_input("দ্বিতীয় সংখ্যাটি লিখুন: ")

        result = None
        op_symbol = ""

        if choice == "1":
            result = add(num1, num2)
            op_symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op_symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op_symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op_symbol = "/"
        elif choice == "5":
            result = power(num1, num2)
            op_symbol = "^"

        if result is not None:
            # সুন্দর ফরম্যাটিং: পূর্ণসংখ্যা হলে int আকারে দেখাবে
            formatted_res = int(result) if result.is_integer() else round(result, 4)
            print(f"\n✅ ফলাফল: {num1} {op_symbol} {num2} = {formatted_res}")


# =====================================================================
# 2. Python Knowledge Quiz Tool
# =====================================================================

def run_quiz() -> None:
    """পাইথন কুইজ সাব-সিস্টেম। প্রশ্ন, স্কোর ট্র্যাকিং ও ফিডব্যাক হ্যান্ডেল করে।"""
    print("\n" + "=" * 50)
    print("      🎯 PYTHON BASICS QUICK QUIZ")
    print("=" * 50)
    print("প্রতিটি প্রশ্নের জন্য (A, B, C, D) এর মধ্যে সঠিক উত্তর দিন।")

    # কুইজের প্রশ্নের তালিকা (Question Bank)
    quiz_data = [
        {
            "question": "1. Python এ ভ্যারিয়েবলের টাইপ জানতে কোন বিল্ট-ইন ফাংশন ব্যবহৃত হয়?",
            "options": ["A) typeof()", "B) type()", "C) check_type()", "D) var_type()"],
            "answer": "B",
            "explanation": "Python-এ type(variable_name) দিয়ে টাইপ দেখা হয়।"
        },
        {
            "question": "2. নিচের কোন লুপটি নির্দিষ্ট শর্ত False না হওয়া পর্যন্ত চলতেই থাকে?",
            "options": ["A) for loop", "B) do-while loop", "C) while loop", "D) foreach loop"],
            "answer": "C",
            "explanation": "while <condition>: শর্তটি True থাকা পর্যন্ত বারবার ঘুরে।"
        },
        {
            "question": "3. ফাংশনে অনির্দিষ্ট সংখ্যক পজিশনাল আর্গুমেন্ট গ্রহণ করতে কোনটি ব্যবহৃত হয়?",
            "options": ["A) *args", "B) **kwargs", "C) &args", "D) ...args"],
            "answer": "A",
            "explanation": "*args পজিশনাল আর্গুমেন্টকে tuple হিসেবে গ্রহণ করে।"
        },
        {
            "question": "4. লুপের বর্তমান ধাপ স্কিপ করে পরবর্তী ধাপে চলে যেতে কোন কি-ওয়ার্ড ব্যবহৃত হয়?",
            "options": ["A) break", "B) exit", "C) pass", "D) continue"],
            "answer": "D",
            "explanation": "continue বর্তমান ইটারেশন বাদ দিয়ে পরবর্তী ইটারেশনে নিয়ে যায়।"
        },
        {
            "question": "5. bool('') এর রিটার্ন ভ্যালু কী হবে?",
            "options": ["A) True", "B) False", "C) None", "D) Error"],
            "answer": "B",
            "explanation": "Python-এ ফাঁকা স্ট্রিং ('') falsy ভ্যালু, তাই False রিটার্ন করে।"
        }
    ]

    score = 0
    total_questions = len(quiz_data)

    for q in quiz_data:
        print(f"\n{q['question']}")
        for opt in q["options"]:
            print(f"   {opt}")

        while True:
            user_ans = input("আপনার উত্তর (A/B/C/D): ").strip().upper()
            if user_ans in {"A", "B", "C", "D"}:
                break
            print("⚠️ অনুগ্রহ করে শুধু A, B, C অথবা D লিখুন!")

        if user_ans == q["answer"]:
            print("🎉 চমৎকার! সঠিক উত্তর।")
            score += 1
        else:
            print(f"❌ ভুল উত্তর! সঠিক উত্তর ছিল: {q['answer']}")
            print(f"💡 ব্যাখ্যা: {q['explanation']}")

    # ফলাফল ও রেটিং প্রদর্শন
    percentage = (score / total_questions) * 100
    print("\n" + "-" * 40)
    print(f"📊 আপনার মোট স্কোর: {score}/{total_questions} ({percentage:.1f}%)")

    if percentage == 100:
        print("🏆 অসাধারণ! আপনি Python Phase 0 পুরোপুরি আয়ত্ত করেছেন!")
    elif percentage >= 60:
        print("👍 ভালো করেছেন! একটু রিভিশন দিলে একদম পারফেক্ট হবে।")
    else:
        print("📚 আরেকবার control_flow.py ও functions_basics.py রিভিশন দিন!")
    print("-" * 40)


# =====================================================================
# 3. Main Dashboard Loop
# =====================================================================

def main() -> None:
    """মেইন এন্ট্রি পয়েন্ট। CLI মেনু পরিচালনা করে।"""
    while True:
        print("\n" + "=" * 55)
        print("   🚀 PYTHON PHASE 0: CLI PRACTICE MILESTONE")
        print("=" * 55)
        print("মেনু থেকে যেকোনো একটি অপশন বেছে নিন:")
        print("  [1] 🧮 Mini CLI Calculator")
        print("  [2] 🎯 Python Basics Quiz Tool")
        print("  [3] 🚪 Exit Application")

        user_choice = input("\nআপনার পছন্দ (1, 2, বা 3): ").strip()

        if user_choice == "1":
            run_calculator()
        elif user_choice == "2":
            run_quiz()
        elif user_choice == "3":
            print("\n👋 ধন্যবাদ! প্র্যাকটিস চালিয়ে যান। গুড লাক!\n")
            sys.exit(0)
        else:
            print("⚠️ সঠিক অপশন সিলেক্ট করুন (1, 2, অথবা 3)।")


if __name__ == "__main__":
    main()
