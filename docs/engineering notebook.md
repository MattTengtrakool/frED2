## Apr 30: Project defination

Here's a detailed step-by-step guide to create a course-specific teaching assistant (TA) chatbot based on ChatGPT:

1. Define the scope and objectives:

   - Determine the specific course or subject area the chatbot will cover.
   - Define the chatbot's primary objectives, such as answering questions, providing resources, or assisting with assignments.
2. Collect data:

   - Gather relevant course materials, including lecture notes, slides, textbooks, and Q&A from previous course iterations.
   - Collect examples of both on-topic and off-topic student questions, as well as their corresponding answers or responses.
3. Preprocess data:

   - Clean and format the data into a structured, conversational format.
   - Organize the data into pairs of questions and answers, as well as examples of unrelated questions and appropriate responses.
   - Create metadata or tags to identify different types of questions and responses, such as content-related, off-topic, or hint-providing.
4. Split the dataset:

   - Divide the dataset into training, validation, and testing sets to effectively fine-tune and evaluate the model's performance.
5. Fine-tune the model:

   - Choose a suitable pre-trained model, like ChatGPT or another variant of the GPT architecture.
   - Fine-tune the model with the training set to adapt its knowledge to the specific course content.
   - Monitor the model's performance on the validation set and adjust hyperparameters as necessary to optimize its accuracy and relevance.
6. Set boundaries and rules:

   - Implement a set of criteria or rules to identify off-topic questions or situations where the chatbot should not provide a direct answer.
   - Incorporate these rules into the chatbot's logic or through a separate module that filters and processes incoming questions.
7. Test the chatbot:

   - Evaluate the chatbot's performance using the test set.
   - Conduct user testing with students or other individuals familiar with the course content to assess the chatbot's real-world performance and gather feedback.
8. Iterate and improve:

   - Analyze the feedback and performance metrics from the testing phase to identify areas for improvement.
   - Make necessary adjustments to the chatbot's behavior, fine-tuning process, or rules to address any identified shortcomings.
9. Deploy the chatbot:

   - Integrate the chatbot into a suitable platform or interface, such as a course website, learning management system, or messaging app.
   - Provide clear instructions and guidelines for students on how to use the chatbot and what to expect from it.
10. Monitor and maintain:

- Continuously monitor the chatbot's performance and gather user feedback to identify any emerging issues or areas for improvement.
- Update the chatbot with new course materials or adjustments to the rules and boundaries as necessary to maintain its relevance and effectiveness.

# Usage

To run the program, run the following commands, 


## May 1 - Matt notes

- Implemented backend using Flask and GPT-3.5-turbo model
- Created a functional frontend interface with HTML, CSS, and JavaScript
- Integrated user input and chatbot responses in the UI
  Added a flag button for users to provide feedback on chatbot responses
- Implemented a feedback form that toggles on and off when the flag button is clicked
- Included preset questions for users to quickly ask the chatbot
- Added a loading animation in the response box to improve user experience
  Things I want to Add:

1. Expand the preset questions:

- Include additional preset questions tailored to each section and subsection.
- Organize these questions into categories for easier navigation.
- Implement a dropdown menu or collapsible panels for users to explore section-specific questions.

2. Create a guided walkthrough feature:

- Design a step-by-step tutorial that users can follow to learn about each section and subsection.
- Offer a "next" button that guides users through a series of questions and explanations.
- Allow users to skip steps or jump to a specific section if they prefer.

3. Enhance chatbot's knowledge:

- Provide the chatbot with more training data relevant to each section and subsection.
- Fine-tune the model to understand section-related context and provide more accurate answers.
- Add a table of contents or navigation menu:

4. Implement a navigation menu on the app's interface to allow users to jump directly to a specific section or subsection.
   The menu can be a sidebar, a dropdown, or a collapsible panel.
5. Personalize the user experience:

- Allow users to save their progress, favorite questions, or bookmark sections for easy reference.
- Enable users to set their preferences for the types of content they'd like to explore.
- Utilize visuals and interactive elements:
- Incorporate images, diagrams, or interactive components to help users better understand each section and subsection.
- Consider using tooltips or pop-ups for additional explanations when necessary.

6. Add more bounding + do research on this

# May 2 - Hilea notes
