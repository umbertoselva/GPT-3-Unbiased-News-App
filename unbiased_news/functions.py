import openai
import streamlit as st

def unbiased_news(prompt):
    augmented_prompt = f"""
    Task 1: Rewrite the news article below to make it more informative, 
    fact-focused, truth-focused, unbiased and neutral,
    in doing so make sure that you remove all instances of sensationalism, opinionated language, 
    speculation, unsupported claims, emotional language, moralistic language, personal and anecdotal evidence,
    ideological bias, political bias, confirmation bias, selective reporting,
    false balance, framing bias, emotional bias, outrage bias, groupthink bias,
    hasty generalizations, outlier bias, stereotyping, narrative bias, bandwagon bias, 
    fear-mongering bias, clickbait bias,
    and other similar forms of bias,
    if they are present in the news article.

    
    Task 2: Describe the bias of the original news article
    by using a numbered list containing up to 5 items 
    each dedicated to one form of bias if present in the original news article
    (e.g. 1. Sensationalism: followed by a description;
    2. Opinionated language: followed by a description;
    3. Unbalanced perspective: followed by a description;
    etc.).
    

    Task 3: List and describe up to 5 logical fallacies 
    such as Ad Hominem, Appeal to Authority, Appeal to Fear, Appeal to Ignorance,
    Appeal to Popularity, Argument from Ignorance, Argument from Silence, Argumentum ad Nauseam,
    Bandwagon Fallacy, Begging the Question, Biased Sample, Black-and-White Fallacy, Burden of Proof,
    Circular Reasoning, Composition fallacy, Confirmation Bias, Correlation/Causation Fallacy,
    False Analogy, False Dilemma, False Cause, Gambler's Fallacy, Genetic Fallacy,
    Guilt by association, Hasty Generalization, Loaded Question,
    Middle Ground Fallacy, Misleading Vividness, Moving the Goalposts
    Naturalistic Fallacy, Non Sequitur, No True Scotsman
    Post Hoc, Personal Attack, Poisoning the Well, Proof by Verbosity
    Red Herring, Reductio ad Hitlerum, 
    Slippery Slope, Straw Man, Suppressed Evidence, 
    Texas Sharpshooter, Tu Quoque, Two Wrongs Make a Right, Unrepresentative Sample,
    Weak Analogy, Wishful Thinking,
    if they are present in the original news article.

    
    Your output should have the following structure:

    [1] Unbiased version of the article:

    Here there should be the rewritten article.

    [2] Bias analysis:

    Here there should be the numbered list with the description of the bias in the original news article.

    [3] Logical fallacies:

    Here there should be numbered list with the logical fallacies found in the original news article.

    
    Original news article: 
    {prompt}
    """

    try:
        st.session_state["unbiased_news"] = openai.Completion.create(
            model="text-davinci-003",
            prompt=augmented_prompt,
            temperature=0,
            max_tokens=2000,
        )["choices"][0]["text"]
    except:
        st.write('There was an error =(')
