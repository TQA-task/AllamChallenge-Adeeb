
<img src="https://raw.githubusercontent.com/TQA-task/AllamChallenge-Adeeb/refs/heads/main/1.jpeg" alt="Adeeb" width="300"/>


# Adeeb: AI-Powered Arabic Poetry Generator

An AI-based system designed to generate Arabic poetry that aligns with traditional poetic rules and structures. This project aids users in creating cohesive, contextually meaningful, and rhythmically accurate lines of poetry, enhancing compositions with verses that respect the rhythm, meter, and rhyme of Arabic poetry.
نظام يعتمد على الذكاء الاصطناعي لتوليد الأبيات الشعرية العربية بما يتوافق مع قواعد الشعر التقليدية. يهدف المشروع إلى مساعدة المستخدمين على إكمال قصائدهم بإضافة أبيات متناسقة ومتوافقة مع الوزن والقافية والسياق الشعري.


## Table of Contents

- [Team Members](#team-members)
- [Problem and Solution](#problem-and-solution)
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Data Usage](#data-usage)
- [Data Access and Usage Instructions](#data-access-and-usage-instructions)
- [Summary](#summary)
- [Getting Started](#getting-started)

## Team Members

- Hessa Abdulrahman Alawwad
- Lujain
- Noura
- Lama

## Problem and Solution

يواجه محبو الشعر العربي صعوبة في توليد أبيات تلتزم بالقواعد الشعرية التقليدية. توجد بعض الأدوات لتوليد النصوص، لكنها تفتقر إلى التوازن بين الوزن الشعري والسياق. يسعى هذا المشروع إلى حل هذه المشكلة من خلال:

- تقديم اقتراحات شعرية متوازنة،
- تتبع سلوك المستخدمين والاتجاهات الشعرية،
- توليد أبيات ملائمة لمناسبات خاصة كعيد الفطر واليوم الوطني، مما يعزز من انتشار التطبيق واستخدامه خلال فترات الذروة.


Arabic poetry enthusiasts often find it challenging to generate verses that follow traditional poetic structures. While some text generation tools exist, they often lack the necessary balance between poetic meter and thematic context. This project addresses this gap by:

- Providing well-balanced poetic suggestions,
- Tracking user behavior and poetic trends,
- Generating context-specific verses for special occasions like Eid and National Day, encouraging seasonal engagement and app use.

## Project Description


يهدف هذا المشروع إلى تطوير نظام ذكي لتوليد أبيات شعرية متناسقة. يعتمد النظام على فهم قواعد الشعر، الوزن، والقافية لتقديم اقتراحات أبيات تلائم القصيدة التي يعمل عليها المستخدم. تتضمن الميزات الرئيسية:

- تحليل هيكل الشعر وفهم الفروق الدقيقة بين أشكال الشعر العربي المختلفة.
- مساعدة الشعراء على إكمال قصائدهم بأبيات متناسقة وجميلة.
- واجهة تفاعلية للمستخدمين لاستكشاف أفكار شعرية جديدة بشكل منظم وجميل.


This project develops a smart AI system for generating harmonious Arabic poetry lines. The system comprehends poetic rules, meters, and rhymes, offering users verse suggestions that blend seamlessly with their compositions. Key features include:

- Analyzing poetic structure and nuances across Arabic poetry forms.
- Assisting poets in completing their work with aesthetically pleasing, contextually relevant lines.
- A user-friendly interface for exploring poetic creativity in a structured, harmonious way.

## Technologies Used

- **Google Colab**: Model training and experimentation.
- **ALLAM**: Advanced natural language understanding and generation.
- **Gradio**: Interactive interface for generating and testing poetry lines.
- **IBM Watsonx**: AI platform for language processing tasks.
- **Weights & Biases (W&B)**: Experiment tracking and model optimization.
- **APCD Dataset**: Arabic Poetry Corpus Dataset covering poetry from pre-Islamic to modern times.

## Data Usage

The model was trained and evaluated on **APCD** (Arabic Poetry Corpus Dataset), an open-source dataset that spans various historical periods. Predefined and customized time intervals were tested.

## Data Access and Usage Instructions

The dataset is open-source and available on GitHub. To use it:

1. Clone the dataset repository.
2. Load the data into your environment to work with the model.

## Summary

This project provides a unique AI solution for generating Arabic poetry that respects traditional poetic meter and rhyme. The system addresses common challenges in poetry generation by balancing poetic structure with thematic context. Our model achieved an accuracy of **44%**, delivering rhythmically and contextually relevant poetry lines.

## Getting Started

To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/arabic-poetry-generator.git
