import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(
    page_title="Indore Hotel Recommender",
    page_icon="🏨",
    layout="wide"
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .hotel-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .hotel-name {
        font-size: 24px;
        font-weight: bold;
        color: #1e3a8a;
    }
    .hotel-price {
        font-size: 18px;
        font-weight: bold;
        color: #047857;
    }
    .hotel-address {
        font-style: italic;
        color: #4b5563;
    }
    .hotel-features {
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Create a database of hotels in Indore
hotels = [
    {
        "name": "Radisson Blu Hotel Indore",
        "address": "12 Scheme No. 94C, Ring Road, Indore",
        "price_range": "₹6,000 - ₹12,000 per night",
        "rating": 4.5,
        "features": ["Swimming Pool", "Fitness Center", "Spa", "Free Wi-Fi", "Restaurant", "Bar", "Business Center", "Room Service", "Conference Rooms"],
        "description": "A luxury 5-star hotel with modern amenities and excellent service.",
        "location_link": "https://maps.app.goo.gl/SU57VMqfTxSqZeSz5"
    },
    {
        "name": "Sayaji Hotel Indore",
        "address": "H-1, Scheme No 54, Vijay Nagar, Indore",
        "price_range": "₹5,500 - ₹10,000 per night",
        "rating": 4.4,
        "features": ["Swimming Pool", "Fitness Center", "Spa", "Free Wi-Fi", "Multiple Restaurants", "Bar", "Business Center", "Room Service"],
        "description": "One of the finest 5-star hotels in Indore with excellent dining options.",
        "location_link": "https://maps.app.goo.gl/aWSbcxLPgZ43hHDa9"
    },
    {
        "name": "Effotel by Sayaji Indore",
        "address": "4/2 Nath Mandir Road, South Tukoganj, Indore",
        "price_range": "₹3,500 - ₹7,000 per night",
        "rating": 4.2,
        "features": ["Restaurant", "Free Wi-Fi", "Room Service", "Conference Rooms", "Fitness Center", "Bar"],
        "description": "A business hotel offering comfortable accommodation and good amenities.",
        "location_link": "https://maps.app.goo.gl/6xEoKs6bKKGpJDDv5"
    },
    {
        "name": "Lemon Tree Hotel Indore",
        "address": "3 RNT Marg, South Tukoganj, Indore",
        "price_range": "₹3,000 - ₹6,000 per night",
        "rating": 4.1,
        "features": ["Restaurant", "Bar", "Fitness Center", "Free Wi-Fi", "Room Service", "Business Center"],
        "description": "A comfortable hotel with modern amenities and convenient location.",
        "location_link": "https://maps.app.goo.gl/AaHNgUeBPF89iNkW6"
    },
    {
        "name": "Hotel Amar Vilas",
        "address": "1 Old Palasia, Indore",
        "price_range": "₹2,500 - ₹5,000 per night",
        "rating": 4.0,
        "features": ["Restaurant", "Free Wi-Fi", "Room Service", "Parking", "Conference Rooms"],
        "description": "A centrally located hotel with good amenities and comfortable rooms.",
        "location_link": "https://maps.app.goo.gl/sWMLLG9QJ7p9f9WQ9"
    },
    {
        "name": "Fairfield by Marriott Indore",
        "address": "Scheme No. 94C, Ring Road, Indore",
        "price_range": "₹4,500 - ₹9,000 per night",
        "rating": 4.3,
        "features": ["Restaurant", "Fitness Center", "Free Wi-Fi", "Room Service", "Business Center", "Bar"],
        "description": "A premium hotel by Marriott offering excellent service and facilities.",
        "location_link": "https://maps.app.goo.gl/z75ouhKqSoHMtXnA6"
    },
    {
        "name": "Treebo Trend Phoenix",
        "address": "MR 10 Road, Near C21 Mall, Indore",
        "price_range": "₹1,800 - ₹3,500 per night",
        "rating": 3.9,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A budget-friendly hotel offering clean and comfortable rooms.",
        "location_link": "https://maps.app.goo.gl/5xGqn6P9CwKRCMBt8"
    },
    {
        "name": "Golden Gate Hotel",
        "address": "8/2 Navlakha Main Road, Indore",
        "price_range": "₹2,000 - ₹4,000 per night",
        "rating": 3.8,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A mid-range hotel with comfortable rooms and good service.",
        "location_link": "https://maps.app.goo.gl/ZYRxiYQoJzKBYEEP9"
    },
    {
        "name": "Hotel President",
        "address": "163 RNT Marg, South Tukoganj, Indore",
        "price_range": "₹2,500 - ₹5,500 per night",
        "rating": 4.0,
        "features": ["Restaurant", "Free Wi-Fi", "Room Service", "Conference Rooms", "Parking"],
        "description": "A well-maintained hotel with good amenities in the heart of the city.",
        "location_link": "https://maps.app.goo.gl/5QXvUqDdnPECFAZX9"
    },
    {
        "name": "Ginger Hotel Indore",
        "address": "Scheme No. 54, Vijay Nagar, Indore",
        "price_range": "₹2,200 - ₹4,000 per night",
        "rating": 3.9,
        "features": ["Free Wi-Fi", "Restaurant", "Fitness Center", "Room Service", "Parking"],
        "description": "A smart budget hotel offering clean rooms and good basic facilities.",
        "location_link": "https://maps.app.goo.gl/8RYAj7BfFQUEJqkz7"
    },
    {
        "name": "Hotel Shikha",
        "address": "5/2 Manorama Ganj, Indore",
        "price_range": "₹1,500 - ₹3,000 per night",
        "rating": 3.7,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A budget hotel with comfortable rooms in a convenient location.",
        "location_link": "https://maps.app.goo.gl/UKGnZkZZnPTdAyU26"
    },
    {
        "name": "Hotel Sarovar Portico",
        "address": "1 Navlakha Main Road, Indore",
        "price_range": "₹3,500 - ₹7,000 per night",
        "rating": 4.1,
        "features": ["Restaurant", "Free Wi-Fi", "Room Service", "Conference Rooms", "Fitness Center"],
        "description": "A well-maintained business hotel with good amenities and service.",
        "location_link": "https://maps.app.goo.gl/yyLRST9zAUHK9zqo9"
    },
    {
        "name": "WOW Hotel",
        "address": "18/3 New Palasia, Indore",
        "price_range": "₹2,000 - ₹4,000 per night",
        "rating": 3.8,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A mid-range hotel with good facilities and comfortable rooms.",
        "location_link": "https://maps.app.goo.gl/LGEocrZNGbSGTnUj7"
    },
    {
        "name": "Regenta Central Indore",
        "address": "12 Scheme No. 94C, Ring Road, Indore",
        "price_range": "₹3,800 - ₹7,500 per night",
        "rating": 4.2,
        "features": ["Swimming Pool", "Restaurant", "Free Wi-Fi", "Fitness Center", "Bar", "Room Service"],
        "description": "A premium hotel with excellent facilities and comfortable accommodation.",
        "location_link": "https://maps.app.goo.gl/wUXQqHQr1oTRVQvV9"
    },
    {
        "name": "Mangal City Hotel",
        "address": "10 Mangal City, Vijay Nagar, Indore",
        "price_range": "₹2,500 - ₹5,000 per night",
        "rating": 3.9,
        "features": ["Restaurant", "Free Wi-Fi", "Room Service", "Parking", "Conference Rooms"],
        "description": "A comfortable hotel with good amenities and convenient location.",
        "location_link": "https://maps.app.goo.gl/78qfcYTnXCe4sEWY8"
    },
    {
        "name": "Hotel Infinity",
        "address": "22 Bhawarkuan Main Road, Indore",
        "price_range": "₹2,200 - ₹4,500 per night",
        "rating": 3.8,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A mid-range hotel offering good value for money and comfortable stays.",
        "location_link": "https://maps.app.goo.gl/iV4LXEPA1XrGRoXB8"
    },
    {
        "name": "Hotel Ambassador",
        "address": "163 MG Road, Indore",
        "price_range": "₹2,000 - ₹4,000 per night",
        "rating": 3.7,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A centrally located hotel with comfortable rooms and good basic amenities.",
        "location_link": "https://maps.app.goo.gl/hMGkAxbF9D2pLAKs5"
    },
    {
        "name": "Luxish Hotel",
        "address": "10/1 Patel Marg, Geeta Bhawan, Indore",
        "price_range": "₹1,800 - ₹3,500 per night",
        "rating": 3.6,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Air Conditioning"],
        "description": "A budget-friendly hotel with clean rooms and basic amenities.",
        "location_link": "https://maps.app.goo.gl/uoMnNnRGgXyGFYQK6"
    },
    {
        "name": "Hotel Fortune Landmark",
        "address": "157 Race Course Road, Indore",
        "price_range": "₹4,000 - ₹8,000 per night",
        "rating": 4.2,
        "features": ["Swimming Pool", "Restaurant", "Free Wi-Fi", "Fitness Center", "Bar", "Room Service", "Conference Rooms"],
        "description": "A premium hotel offering excellent facilities and professional service.",
        "location_link": "https://maps.app.goo.gl/9nMGrk9fCEKAQv5j7"
    },
    {
        "name": "Hotel Grand Ashoka",
        "address": "14 Navlakha Main Road, Indore",
        "price_range": "₹2,200 - ₹4,500 per night",
        "rating": 3.8,
        "features": ["Free Wi-Fi", "Restaurant", "Room Service", "Parking", "Conference Rooms"],
        "description": "A well-maintained hotel with good facilities and comfortable rooms.",
        "location_link": "https://maps.app.goo.gl/NTHQpDVaUmXGcCZd7"
    }
]

# Dictionary for hotel features to help in filtering
feature_options = {
    "Swimming Pool": "Swimming Pool",
    "Fitness Center": "Fitness Center",
    "Spa": "Spa",
    "Free Wi-Fi": "Free Wi-Fi",
    "Restaurant": "Restaurant",
    "Bar": "Bar",
    "Business Center": "Business Center",
    "Room Service": "Room Service",
    "Conference Rooms": "Conference Rooms",
    "Parking": "Parking",
    "Air Conditioning": "Air Conditioning"
}

# Store conversational history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Indore Hotel Recommendation Assistant. I can help you find the perfect hotel for your stay in Indore. What are you looking for in a hotel? (e.g., budget range, specific facilities, location preferences)"}
    ]

# Sidebar for filters
st.sidebar.title("Hotel Filters")

# Price range filter
price_min = st.sidebar.slider("Minimum Price (₹)", 1000, 10000, 1000, 500)
price_max = st.sidebar.slider("Maximum Price (₹)", 1000, 12000, 12000, 500)

# Star rating filter
min_rating = st.sidebar.slider("Minimum Rating", 3.0, 5.0, 3.5, 0.1)

# Features filter
selected_features = st.sidebar.multiselect(
    "Hotel Features",
    options=list(feature_options.keys()),
    default=[]
)

# Button to apply filters
if st.sidebar.button("Apply Filters"):
    # Filter hotels based on criteria
    filtered_hotels = []
    for hotel in hotels:
        # Extract minimum price from range (removing ₹ and converting to int)
        price_range = hotel["price_range"]
        min_price = int(price_range.split(" - ")[0].replace("₹", "").replace(",", ""))
        max_price = int(price_range.split(" - ")[1].split(" ")[0].replace("₹", "").replace(",", ""))
        
        # Check if hotel meets criteria
        if (min_price >= price_min and max_price <= price_max and 
            hotel["rating"] >= min_rating and
            (not selected_features or all(feature in hotel["features"] for feature in selected_features))):
            filtered_hotels.append(hotel)
    
    # Add system message about filtered results
    filter_message = f"Found {len(filtered_hotels)} hotels matching your criteria."
    st.session_state.messages.append({"role": "assistant", "content": filter_message})
    
    # Display filtered hotels
    if filtered_hotels:
        hotel_names = [hotel["name"] for hotel in filtered_hotels]
        hotel_list = ", ".join(hotel_names)
        recommendation = f"Here are some hotels that match your criteria: {hotel_list}. Ask me about any specific hotel for more details!"
        st.session_state.messages.append({"role": "assistant", "content": recommendation})

# Main page title
st.title("🏨 Indore Hotel Recommender")
st.write("Find the perfect hotel for your stay in Indore!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Function to get hotel information
def get_hotel_info(hotel_name):
    for hotel in hotels:
        if hotel_name.lower() in hotel["name"].lower():
            return hotel
    return None

# Function to check if a question is about hotels
def is_hotel_related(question):
    hotel_keywords = ["hotel", "stay", "accommodation", "room", "book", "reserve", "lodging", "inn", "resort"]
    location_keywords = ["indore", "madhya pradesh"]
    query_keywords = ["recommend", "suggest", "find", "best", "top", "luxury", "budget", "cheap", "expensive"]
    facility_keywords = ["pool", "wifi", "restaurant", "gym", "fitness", "spa", "parking", "air conditioning"]
    
    # Convert question to lowercase for case-insensitive matching
    question_lower = question.lower()
    
    # Check if question contains hotel-related keywords
    contains_hotel = any(keyword in question_lower for keyword in hotel_keywords)
    contains_location = any(keyword in question_lower for keyword in location_keywords)
    contains_query = any(keyword in question_lower for keyword in query_keywords)
    contains_facility = any(keyword in question_lower for keyword in facility_keywords)
    
    return contains_hotel or (contains_location and (contains_query or contains_facility))

# Function to provide hotel recommendations based on input
def get_recommendations(user_input):
    user_input_lower = user_input.lower()
    
    # Check if asking about a specific hotel
    for hotel in hotels:
        if hotel["name"].lower() in user_input_lower:
            return f"Here is information about {hotel['name']}:\n\n" + \
                   f"- Rating: {hotel['rating']} stars\n" + \
                   f"- Price Range: {hotel['price_range']}\n" + \
                   f"- Address: {hotel['address']}\n" + \
                   f"- Features: {', '.join(hotel['features'])}\n" + \
                   f"- Description: {hotel['description']}\n" + \
                   f"- Location: [View on Map]({hotel['location_link']})\n\n" + \
                   f"Would you like to know more about this hotel or any other hotels in Indore?"
    
    # Check if asking about budget hotels
    if any(word in user_input_lower for word in ["budget", "cheap", "affordable", "inexpensive"]):
        budget_hotels = [hotel for hotel in hotels if "₹3,000" in hotel["price_range"]]
        hotels_list = ", ".join([hotel["name"] for hotel in budget_hotels[:5]])
        return f"Here are some budget-friendly hotels in Indore: {hotels_list}. Would you like more details about any of these hotels?"
    
    # Check if asking about luxury hotels
    if any(word in user_input_lower for word in ["luxury", "premium", "5 star", "five star", "high-end"]):
        luxury_hotels = [hotel for hotel in hotels if hotel["rating"] >= 4.2]
        hotels_list = ", ".join([hotel["name"] for hotel in luxury_hotels[:5]])
        return f"Here are some luxury hotels in Indore: {hotels_list}. Would you like more details about any of these hotels?"
    
    # Check if asking about specific features
    for feature in feature_options:
        if feature.lower() in user_input_lower:
            feature_hotels = [hotel for hotel in hotels if feature in hotel["features"]]
            hotels_list = ", ".join([hotel["name"] for hotel in feature_hotels[:5]])
            return f"Here are some hotels in Indore with {feature}: {hotels_list}. Would you like more details about any of these hotels?"
    
    # If it's a hotel-related question but not specific
    if is_hotel_related(user_input):
        random_hotels = random.sample(hotels, 5)
        hotels_list = ", ".join([hotel["name"] for hotel in random_hotels])
        return f"Here are some popular hotels in Indore: {hotels_list}. Would you like more details about any of these hotels or do you have specific requirements?"
    
    # If not a hotel-related question
    return "I'm here to help you find the perfect hotel in Indore. Could you please specify what kind of hotel you're looking for? For example, you can ask about budget hotels, luxury hotels, or hotels with specific features like a swimming pool."

# User input
user_input = st.chat_input("Ask about hotels in Indore...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Check if user is asking about a specific hotel
    specific_hotel = None
    for hotel in hotels:
        if hotel["name"].lower() in user_input.lower():
            specific_hotel = hotel
            break
    
    # Generate response
    if specific_hotel:
        # If asking about a specific hotel, show hotel card
        with st.chat_message("assistant"):
            st.write(f"Here is information about {specific_hotel['name']}:")
            
            st.markdown(f"<div class='hotel-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='hotel-name'>{specific_hotel['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='hotel-price'>{specific_hotel['price_range']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='hotel-address'>{specific_hotel['address']}</div>", unsafe_allow_html=True)
            st.write(f"**Rating:** {specific_hotel['rating']} ⭐")
            st.write(f"**Description:** {specific_hotel['description']}")
            st.write(f"**Features:**")
            st.write(", ".join(specific_hotel['features']))
            st.markdown(f"[View on Map]({specific_hotel['location_link']})")
            st.markdown(f"</div>", unsafe_allow_html=True)
        
        # Add response to chat history
        response_text = f"I've shown you details about {specific_hotel['name']}. Is there anything specific you'd like to know about this hotel or would you like to see other options?"
        st.session_state.messages.append({"role": "assistant", "content": response_text})
        
        # Display response
        with st.chat_message("assistant"):
            st.write(response_text)
    else:
        # Get general recommendations
        response = get_recommendations(user_input)
        
        # Add response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Display response
        with st.chat_message("assistant"):
            st.write(response)
            
            # If it's a general query, show a few hotel cards
            if is_hotel_related(user_input) and "specific hotel" not in response:
                st.write("Here are some hotel options you might be interested in:")
                
                sample_hotels = random.sample(hotels, 3)
                
                for hotel in sample_hotels:
                    st.markdown("""<hr style="height:1px;border:none;color:#ddd;background-color:#ddd;" />""", unsafe_allow_html=True)
                    st.markdown(f"<div class='hotel-card'>", unsafe_allow_html=True)
                    st.markdown(f"<div class='hotel-name'>{hotel['name']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='hotel-price'>{hotel['price_range']}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='hotel-address'>{hotel['address']}</div>", unsafe_allow_html=True)
                    st.write(f"**Rating:** {hotel['rating']} ⭐")
                    st.write(f"**Features:** {', '.join(hotel['features'][:5])}")
                    st.markdown(f"[View on Map]({hotel['location_link']})")
                    st.markdown(f"</div>", unsafe_allow_html=True)

# Instructions section
with st.expander("How to use this chatbot"):
    st.write("""
    1. **Ask about hotels in Indore**: You can ask for recommendations based on your preferences like budget, facilities, or location.
    2. **Filter hotels**: Use the sidebar filters to narrow down your search based on price, rating, and features.
    3. **Get specific information**: Ask about a specific hotel by name to see detailed information.
    4. **Examples of questions you can ask**:
       - "Show me luxury hotels in Indore"
       - "What are the best hotels with swimming pools?"
       - "Tell me about Radisson Blu Hotel"
       - "What are some budget-friendly hotels in Indore?"
       - "Which hotels have conference facilities?"
    """)

# Footer
st.markdown("""---
Made with ❤️ for Indore tourists
""")
