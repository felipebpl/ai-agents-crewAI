# Final Project: AI Agents for Lifelong Learning  

## The Problem  

Lifelong learning depends not just on access to information, but on consistent exposure to **relevant, up-to-date content** that aligns with individual interests and contributes meaningfully to personal and professional growth.  

While information is abundant, there’s no solution that effectively curates **up-to-date, relevant content** tailored to evolving interests.  

I’ve faced this pain point firsthand. Staying current with newsletters, research updates, and niche discussions is overwhelming and inefficient. 

This project addresses a critical gap: leveraging the constant flow of new content to accelerate learning in a way that is personalized, actionable, and aligned with long-term growth.  



## The Solution  

This project introduces a **multi-agent system** designed to act as a learning companion, curating and delivering content that supports continuous, personalized education. Using **Langchain, FireCrwaler open source, openAI API**, we build a system that:  

1. **Query Content**: Dynamically retrieves articles, memos, and updates from diverse, high-quality sources like Hacker News and professional newsletters. 

2. **Filters for Relevance**: Identifies the most pertinent content aligned with user-defined learning goals and interests.  

3. **Summarizes for Precision**: Assemble the final output, providing concise overviews from the filters, enabling users to quickly assess the value of each piece while linking to the original material for deeper exploration.  

4. **Notifier Agent**:  sends the summaries to the user via WhatsApp for seamless accessibility.


## How It Works  

The system leverages the synergy of **AI agents** and **Large Language Models (LLMs)** to ensure relevance and adaptability:  

- **Fetcher Agent**: Collects content from predefined sources, ensuring a consistent and diverse stream of information.  
- **Filter Agent**: Evaluates and prioritizes content based on relevance to user preferences and learning goals.  
- **Summarizer Agent**: Distills selected content into concise summaries, retaining key insights for quick and effective understanding.  
- **Notifier Agent**: Logs curated content and sends summaries to the user via WhatsApp for seamless accessibility.  

## Impact on Lifelong Learning  

This system supports lifelong learning by:  
1. **Promoting Focus**: Reducing noise and information overload by prioritizing relevant content.  
2. **Encouraging Exploration**: Suggesting diverse sources and materials tailored to specific interests.  
3. **Adapting Over Time**: Growing alongside the user’s learning journey, offering increasingly precise recommendations.  

## Evaluation Metrics  

The success of this project will be measured by:  
1. **Relevance Accuracy**: At least 90% of recommendations align with user interests.  
2. **Engagement**: Users interact with >80% of delivered content through summaries or full articles.  
3. **Feedback Adaptability**: The system demonstrates a measurable improvement in relevance precision over time.  

---

## Final Goal  

To create a precise, adaptable, and user-focused system that empowers lifelong learners by seamlessly integrating relevant, high-quality content into their daily routines.  

This project emphasizes the transformative power of AI in shaping learning habits, demonstrating that with the right tools, lifelong learning can become not just a goal, but a natural and effortless part of life.  

---

### Repository  
[ai-agents-crewAI](https://github.com/felipebpl/ai-agents-crewAI)  

## Structure of the project
ai_learning_companion/
├── agents/
│   ├── __init__.py
│   ├── content_fetcher.py
│   ├── content_filter.py
│   ├── summarizer.py
│   └── notifier.py
├── utils/
│   ├── __init__.py
│   └── config.py
│   └── openai_client.py
│   └── markdown_cleaner.py
├── main.py
├── requirements.txt

## How to run

1. **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment**:
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

3. **Install the Requirements**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Main Script**:
    ```bash
    python main.py
    ```
