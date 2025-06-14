import openai

userInput = """[Opening]
Jacob: Good afternoon, everyone. Thanks for joining. Let’s get started
Sarah: Afternoon, Jacob. Hope everyone’s doing well.
Jacob: Today, we’ll cover project updates, roadblocks, and next steps. Let’s dive in.
[Project Updates]
Sarah: The development team has completed the database integration. Kevin, any highlights?
Kevin: Yes. We\'ve optimized the queries, reducing load time by 30%.
Mia: That’s fantastic! The design team is finalizing UI elements based on feedback.
Alex: Marketing has started drafting messaging for the product launch.
Jacob: Great progress! Any roadblocks?
[Challenges]
Kevin: We’re facing a bug with the authentication flow.
Sarah: Got it. Can we prioritize that this week?
Mia: I need clarity on the new brand guidelines before finalizing designs.
Alex: Let’s set up a quick sync with leadership tomorrow.
[Next Steps]
Jacob: Action items: Kevin to debug authentication, Mia to refine UI, Alex to finalize messaging.
Sarah: Let’s aim to resolve these by Friday.
Jacob: Sounds good. Anything else?
Kevin: No, that covers it.
Mia: Thanks, everyone!
Jacob: Appreciate your time. Meeting adjourned."""

try:
  completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    store=True,
    messages=[
      {"role": "system", "content": "Write a 3 bullet point summary based on the prompt the user inputs."},
      {"role": "user", "content": userInput}
    ]
  )
except Exception as e:
  print("Did not work!!!")
  print(e)

if __name__ == "__main__":
    print(completion.choices[0].message.content);