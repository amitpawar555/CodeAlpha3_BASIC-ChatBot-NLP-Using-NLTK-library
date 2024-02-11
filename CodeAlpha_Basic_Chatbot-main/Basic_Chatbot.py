import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, how about you?"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me a chatbot.", "I'm just a chatbot.", "I go by the name chatbot."]
    ],
    [
        r"(.*) (help|support)",
        ["Sure, I can help you. What do you need assistance with?", "How can I assist you?"]
    ],
    [
        r"quit|exit",
        ["Bye, take care!", "Goodbye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that.", "Can you please rephrase that?"]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with any questions or concerns you may have."]
    ],
    [
        r"what (.*) like ?",
        ["I like helping people and having conversations."]
    ],
    [
        r"how (.*) help ?",
        ["You can ask me anything, and I'll do my best to assist you."]
    ],
    [
        r"thanks|thank you",
        ["You're welcome!", "No problem!", "Anytime!"]
    ],
    [
        r"how old are you ?",
        ["I'm just a program, so I don't have an age."]
    ],
    [
        r"who created you ?",
        ["I was created by a team of developers."]
    ],
    [
        r"(.*) weather (.*) today ?",
        ["You can check the weather using various online services."]
    ],
    [
        r"(.*) (movie|film) (.*) recommend ?",
        ["It depends on your preferences. What genre do you like?"]
    ],
    [
        r"(.*) (genre) (.*) like ?",
        ["I enjoy a variety of genres, including science fiction, comedy, and drama."]
    ],
    [
        r"(.*) (book|novel) (.*) recommend ?",
        ["There are many great books out there. What type of book are you interested in?"]
    ],
    [
        r"(.*) (sport) (.*) like ?",
        ["I'm just a chatbot, so I don't participate in sports. But I can provide information about them!"]
    ],
    [
        r"(.*) (music) (.*) like ?",
        ["I don't have personal preferences, but I can recommend various genres of music."]
    ],
    [
        r"(.*) (play|listen to) (music|songs) (.*)",
        ["You can listen to music on various streaming platforms like Spotify or Apple Music."]
    ],
    [
        r"(.*) (watch) (movie|film) (.*)",
        ["You can watch movies on streaming platforms like Netflix or Amazon Prime Video."]
    ],
    [
        r"(.*) (read|find) (book|novel) (.*)",
        ["You can find books at your local library or online bookstores like Amazon."]
    ],
    [
        r"(.*) (recipe) (.*)",
        ["You can find recipes on cooking websites or apps like AllRecipes or Tasty."]
    ],
    [
        r"(.*) (learn|study) (.*)",
        ["You can learn a wide range of topics online through courses on platforms like Coursera or Udemy."]
    ],
    [
        r"(.*) (news) (.*)",
        ["You can stay updated on the latest news through news websites or apps."]
    ],
    [
        r"(.*) (joke|funny) (.*)",
        ["Why don't scientists trust atoms? Because they make up everything!"]
    ],
    [
        r"(.*) (quote) (.*)",
        ["\"The only way to do great work is to love what you do.\" - Steve Jobs"]
    ],
    [
        r"(.*) (love) (.*)",
        ["Love is a wonderful thing!"]
    ],
    [
        r"(.*) (hate) (.*)",
        ["Hate is a strong emotion."]
    ],
    [
        r"(.*) (happy|joy) (.*)",
        ["Happiness is contagious!"]
    ],
    [
        r"(.*) (sad|unhappy) (.*)",
        ["I'm sorry to hear that."]
    ],
    [
        r"(.*) (angry|mad) (.*)",
        ["Take a deep breath and try to stay calm."]
    ],
    [
        r"(.*) (bored) (.*)",
        ["Try finding a new hobby or activity to keep yourself entertained!"]
    ],
    [
        r"(.*) (sleepy) (.*)",
        ["You might need some rest."]
    ],
    [
        r"(.*) (hungry) (.*)",
        ["It might be time for a snack!"]
    ],
    [
        r"(.*) (thirsty) (.*)",
        ["Stay hydrated and drink some water!"]
    ],
    [
        r"(.*) (goodbye|bye) (.*)",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*) (food) (.*)",
        ["What type of food are you in the mood for?"]
    ],
    [
        r"(.*) (movie|film) (.*) recommend ?",
        ["How about watching a classic like The Godfather or a recent release like Parasite?"]
    ],
    [
        r"(.*) (TV series|show) (.*) recommend ?",
        ["I recommend checking out popular series like Game of Thrones or Breaking Bad."]
    ],
    [
        r"(.*) (exercise|workout) (.*) recommend ?",
        ["You can try activities like jogging, yoga, or bodyweight exercises."]
    ],
    [
        r"(.*) (game) (.*) recommend ?",
        ["There are many great games out there. What genre are you interested in?"]
    ],
    [
        r"(.*) (hobby) (.*)",
        ["Hobbies are a great way to relax and have fun. What are your interests?"]
    ],
    [
        r"(.*) (travel|trip) (.*) recommend ?",
        ["You can visit popular destinations like Paris, New York, or Tokyo."]
    ],
    [
        r"(.*) (study|learn) (language) (.*) recommend ?",
        ["You can use language learning apps like Duolingo or Rosetta Stone."]
    ],
    [
        r"(.*) (pet) (.*) recommend ?",
        ["Pets can bring joy and companionship. Consider adopting a dog or cat from a shelter."]
    ],
    [
        r"(.*) (coffee) (.*) recommend ?",
        ["You can try popular coffee chains like Starbucks or local cafes in your area."]
    ],
    [
        r"(.*) (tea) (.*) recommend ?",
        ["You can try a variety of teas, such as green tea, black tea, or herbal tea."]
    ],
    [
        r"(.*) (dessert) (.*) recommend ?",
        ["You can indulge in desserts like ice cream, cake, or pastries."]
    ],
    [
        r"(.*) (snack) (.*) recommend ?",
        ["You can enjoy snacks like chips, popcorn, or fruit."]
    ],
    [
        r"(.*) (restaurant) (.*) recommend ?",
        ["You can try restaurants serving cuisines like Italian, Mexican, or Japanese."]
    ],
    [
        r"(.*) (holiday|vacation) (.*) recommend ?",
        ["Consider visiting destinations known for their scenic beauty or cultural heritage."]
    ],
    [
        r"(.*) (exercise|workout) (.*)",
        ["Regular exercise is important for maintaining physical and mental health."]
    ],
    [
        r"(.*) (game) (.*)",
        ["Playing games can be a fun way to relax and unwind."]
    ],
    [
        r"(.*) (hobby) (.*)",
        ["Hobbies are a great way to pursue your interests and passions."]
    ],
    [
        r"(.*) (study|learn) (language) (.*)",
        ["Learning a new language can broaden your horizons and open up new opportunities."]
    ],
    [
        r"(.*) (pet) (.*)",
        ["Pets can provide companionship, love, and joy."]
    ],
    [
        r"(.*) (coffee) (.*)",
        ["Coffee is a popular beverage enjoyed by many people around the world."]
    ],
    [
        r"(.*) (tea) (.*)",
        ["Tea is a soothing beverage that comes in many varieties and flavors."]
    ],
    [
        r"(.*) (dessert) (.*)",
        ["Desserts are a delicious way to satisfy your sweet tooth."]
    ],
    [
        r"(.*) (snack) (.*)",
        ["Snacks are perfect for satisfying hunger between meals."]
    ],
    [
        r"(.*) (restaurant) (.*)",
        ["Restaurants offer a wide range of delicious dishes to suit every palate."]
    ],
    [
        r"(.*) (holiday|vacation) (.*)",
        ["Holidays and vacations are a great time to relax, recharge, and explore new places."]
    ],
    [
        r"(.*) (work) (.*)",
        ["It's important to find a balance between work and personal life."]
    ],
    [
        r"(.*) (family) (.*)",
        ["Family is important for love, support, and connection."]
    ],
    [
        r"(.*) (friend) (.*)",
        ["Friends are an important part of life for companionship and shared experiences."]
    ],
    [
        r"(.*) (stress) (.*)",
        ["It's important to find healthy ways to cope with stress, such as exercise or meditation."]
    ],
    [
        r"(.*) (anxiety) (.*)",
        ["If you're experiencing anxiety, it's important to reach out to a trusted friend or professional for support."]
    ],
    [
        r"(.*) (depression) (.*)",
        ["Depression is a serious mental health condition that requires professional treatment and support."]
    ],
    [
        r"(.*) (sleep) (.*)",
        ["A good night's sleep is essential for overall health and well-being."]
    ],
    [
        r"(.*) (dream) (.*)",
        ["Dreams can provide insight into our subconscious thoughts and desires."]
    ],
    [
        r"(.*) (health) (.*)",
        ["Taking care of your health is important for a fulfilling and happy life."]
    ],
    [
        r"(.*) (exercise) (.*)",
        ["Regular exercise is beneficial for both physical and mental health."]
    ],
    [
        r"(.*) (meditate|meditation) (.*)",
        ["Meditation can help reduce stress and promote relaxation."]
    ],
    [
        r"(.*) (yoga) (.*)",
        ["Yoga is a great way to improve flexibility, strength, and mental clarity."]
    ],
    [
        r"(.*) (hike|hiking) (.*)",
        ["Hiking is a wonderful way to connect with nature and stay active."]
    ],
    [
        r"(.*) (nature) (.*)",
        ["Spending time in nature can have numerous benefits for physical and mental health."]
    ],
    [
        r"(.*) (art) (.*)",
        ["Art can be a powerful form of self-expression and creativity."]
    ],
    [
        r"(.*) (music) (.*)",
        ["Music has the ability to uplift mood and evoke emotions."]
    ],
    [
        r"(.*) (dance) (.*)",
        ["Dancing is a fun way to express yourself and stay active."]
    ],
    [
        r"(.*) (read) (.*)",
        ["Reading is a wonderful way to escape into different worlds and expand your knowledge."]
    ],
    [
        r"(.*) (write) (.*)",
        ["Writing can be a therapeutic outlet for expressing thoughts and emotions."]
    ],
    [
        r"(.*) (travel) (.*)",
        ["Traveling allows you to experience new cultures, cuisines, and landscapes."]
    ],
    [
        r"(.*) (learn) (.*)",
        ["Learning new skills and knowledge can enrich your life and open up new opportunities."]
    ],
    [
        r"(.*) (inspire) (.*)",
        ["Inspiration can come from many sources, including nature, art, and personal experiences."]
    ],
    [
        r"(.*) (motivate) (.*)",
        ["Motivation is the driving force behind achieving goals and dreams."]
    ],
    [
        r"(.*) (relax) (.*)",
        ["Relaxation techniques like deep breathing and mindfulness can help reduce stress and promote calm."]
    ],
    [
        r"(.*) (calm) (.*)",
        ["Finding moments of calmness and tranquility can help restore balance in life."]
    ],
    [
        r"(.*) (mindfulness) (.*)",
        ["Practicing mindfulness involves being present in the moment and observing thoughts and sensations without judgment."]
    ],
    [
        r"(.*) (productivity) (.*)",
        ["Effective time management and organization can boost productivity."]
    ],
    [
        r"(.*) (achieve) (.*)",
        ["Setting clear goals and taking consistent action are key to achieving success."]
    ],
    [
        r"(.*) (success) (.*)",
        ["Success can be defined in many ways and often involves hard work, perseverance, and resilience."]
    ],
    [
        r"(.*) (failure) (.*)",
        ["Failure is a natural part of life and can provide valuable lessons and opportunities for growth."]
    ],
    [
        r"(.*) (self-care) (.*)",
        ["Self-care is essential for maintaining physical, emotional, and mental well-being."]
    ],
    [
        r"(.*) (gratitude) (.*)",
        ["Practicing gratitude can cultivate a positive mindset and increase happiness."]
    ],
    [
        r"(.*) (kindness) (.*)",
        ["Acts of kindness, no matter how small, can make a big difference in someone's day."]
    ],
    [
        r"(.*) (empathy) (.*)",
        ["Empathy involves understanding and sharing the feelings of others."]
    ],
    [
        r"(.*) (community) (.*)",
        ["Building strong communities fosters connection, support, and belonging."]
    ],
    [
        r"(.*) (environment) (.*)",
        ["Protecting the environment is crucial for the well-being of future generations."]
    ],
    [
        r"(.*) (technology) (.*)",
        ["Technology has revolutionized the way we live, work, and communicate."]
    ],
    [
        r"(.*) (future) (.*)",
        ["The future is full of possibilities and opportunities for growth and innovation."]
    ],
    [
        r"(.*) (challenge) (.*)",
        ["Challenges can be opportunities for growth and personal development."]
    ],
    [
        r"(.*) (change) (.*)",
        ["Change is inevitable and can lead to personal and societal transformation."]
    ],
    [
        r"(.*) (mindset) (.*)",
        ["Having a positive mindset can empower you to overcome obstacles and achieve your goals."]
    ],
    [
        r"(.*) (dream) (.*)",
        ["Dream big and pursue your passions with courage and determination."]
    ],
    [
        r"(.*) (improve) (.*)",
        ["Continuous learning and self-improvement are key to personal and professional growth."]
    ],
    [
        r"(.*) (inspiration) (.*)",
        ["Seek inspiration from the world around you and from people who have achieved greatness."]
    ],
    [
        r"(.*) (motivation) (.*)",
        ["Stay motivated by setting clear goals, staying focused, and celebrating progress."]
    ],
    [
        r"(.*) (resilience) (.*)",
        ["Resilience is the ability to bounce back from setbacks and adversity."]
    ],
    [
        r"(.*) (strength) (.*)",
        ["Strength comes from overcoming challenges and embracing your unique qualities."]
    ],
    [
        r"(.*) (courage) (.*)",
        ["Courage is the willingness to face fear and take bold action."]
    ],
    [
        r"(.*) (kindness) (.*)",
        ["Kindness is a powerful force that can create positive change in the world."]
    ],
    [
        r"(.*) (compassion) (.*)",
        ["Compassion involves showing empathy and understanding towards others."]
    ],
    [
        r"(.*) (joy) (.*)",
        ["Find joy in the simple things and cherish moments of happiness."]
    ],
    [
        r"(.*) (peace) (.*)",
        ["Peace begins within and radiates outwards to create harmony in the world."]
    ],
    [
        r"(.*) (love) (.*)",
        ["Love is the most powerful force in the universe."]
    ],
    [
        r"(.*) (purpose) (.*)",
        ["Discover your purpose and live each day with passion and intention."]
    ],
    [
        r"(.*) (creativity) (.*)",
        ["Embrace your creativity and express yourself freely."]
    ],
    [
        r"(.*) (adventure) (.*)",
        ["Life is an adventure waiting to be explored."]
    ],
    [
        r"(.*) (explore) (.*)",
        ["Explore new places, ideas, and experiences to enrich your life."]
    ],
    [
        r"(.*) (wonder) (.*)",
        ["Approach life with a sense of wonder and curiosity."]
    ],
    [
        r"(.*) (curiosity) (.*)",
        ["Curiosity fuels discovery and leads to endless possibilities."]
    ],
    [
        r"(.*) (discover) (.*)",
        ["Discover the beauty and magic of the world around you."]
    ],
    [
        r"(.*) (beauty) (.*)",
        ["Beauty is everywhere, waiting to be appreciated."]
    ],
    [
        r"(.*) (appreciate) (.*)",
        ["Take time to appreciate the blessings and abundance in your life."]
    ],
    [
        r"(.*) (abundance) (.*)",
        ["Abundance flows into your life when you cultivate gratitude and positivity."]
    ],
    [
        r"(.*) (positive) (.*)",
        ["Maintain a positive attitude and focus on the good in every situation."]
    ],
    [
        r"(.*) (growth) (.*)",
        ["Embrace change and challenges as opportunities for personal growth."]
    ],
    [
        r"(.*) (wisdom) (.*)",
        ["Wisdom comes from life experience and reflection."]
    ],
    [
        r"(.*) (knowledge) (.*)",
        ["Seek knowledge and wisdom to enrich your understanding of the world."]
    ],
    [
        r"(.*) (understanding) (.*)",
        ["Seek to understand others and cultivate empathy and compassion."]
    ],
    [
        r"(.*) (balance) (.*)",
        ["Find balance in all areas of your life to maintain harmony and well-being."]
    ],
    [
        r"(.*) (harmony) (.*)",
        ["Harmony arises from inner peace and alignment with your values."]
    ],
    [
        r"(.*) (alignment) (.*)",
        ["Align your actions with your values and goals to create a fulfilling life."]
    ],
    [
        r"(.*) (fulfillment) (.*)",
        ["Find fulfillment in serving others and making a positive impact in the world."]
    ],
    [
        r"(.*) (impact) (.*)",
        ["Your actions have the power to create meaningful change."]
    ]
]

# Create a Chatbot
def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")

    # Create Chat instance
    chat = Chat(pairs, reflections)
    # Start conversation
    chat.converse()

if __name__ == "__main__":
    chatbot()
