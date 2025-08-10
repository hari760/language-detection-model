# Simple Language Detection AI

A rudimentary AI project that teaches computers to recognize different languages with latin text.

## How Our AI Learns

### 🧠 The Learning Process
1. **Study Phase**: We show the AI examples of English and Spanish text
2. **Pattern Recognition**: The AI notices which letter pairs appear most often in each language  
3. **Memory Storage**: It creates a "fingerprint" for each language based on these patterns
4. **Smart Guessing**: When given new text, it compares patterns and makes its best guess!

### 🔍 The Detective Work
Think of it like this: if you see the letter combination "ñ" or "ll", you'd probably guess Spanish, right? Our AI does something similar but with hundreds of letter combinations!

## Project Structure

```
├── sampleText.py       # Training data (teaches the AI what languages look like)
├── utilityFunctions.py # AI brain functions (pattern recognition)  
├── trainModel.py       # AI training bootcamp
└── runModel.py         # Put the AI to the test!
```

## Cool AI Features

- **🌍 Smart Text Cleaning** - Handles weird characters and accents like a pro
- **🔤 Pattern Learning** - Remembers how letters like to appear together
- **⚡ Lightning Fast** - Makes predictions in milliseconds
- **📚 Easy to Teach** - Add new languages by just showing it examples
- **🎯 Pretty Accurate** - Gets it right most of the time!

## Watch the AI in Action

### Quick Demo

```python
from utilityFunctions import detect_language
from trainModel import trainModel

# Train our AI (like sending it to language school!)
ai_brain = trainModel()

# Test it out
mystery_text = "Hola, ¿cómo estás hoy?"
prediction = detect_language(mystery_text, ai_brain)
print(f"The AI thinks this is: {prediction}")
# Output: The AI thinks this is: spanish
```

### Run the Full Demo

```bash
python runModel.py
```

Watch as the AI:
1. 📖 Studies the training examples
2. 🧠 Builds its language knowledge  
3. 🔍 Analyzes a mystery Spanish text
4. 🎉 Successfully identifies it as Spanish!

## How Smart Is This AI?

Our AI currently speaks:
- **English** - Recognizes patterns like "the", "and", "ing"
- **Spanish** - Spots patterns like "que", "con", "ción"

*Want to teach it French or German? Just add some training examples!*

### 🔬 The Algorithm

1. **Text Cleaning**: Removes fancy characters and makes everything lowercase
2. **Pattern Mapping**: Creates a 27×27 grid (26 letters + space) showing which letters follow which
3. **Fingerprinting**: Each language gets its unique "signature" based on these patterns  
4. **Comparison**: Compares new text against known signatures
5. **Best Match**: Picks the closest match - that's the detected language!

### 🤖 Why This Approach Works

Different languages have different strucutres:
- English: loves "th", "er", "ing" 
- Spanish: prefers "qu", "ción", "ll"
- The AI learns these preferences and uses them to make an accurate guess

## Teaching the AI New Languages

Want to expand your AI's vocabulary? Super easy!

```python
# In sampleText.py, just add more examples:
data_train = {
    "english": "The quick brown fox jumps over the lazy dog...",
    "spanish": "El rápido zorro marrón salta sobre el perro perezoso...",
    "french": "Le renard brun rapide saute par-dessus le chien paresseux...",  # New!
}
```

The AI automatically learns the new language - no code changes needed! 🎉

## Plausible Real-World AI Applications

- 📱 **Language detection in social media apps**
- 💬 **Automatic translation triggers in chat apps**  
- 📧 **Email spam filtering by language**
- 🌐 **Website content categorization**
- 📚 **Document organization systems**

## AI Performance Stats

- **Speed**: Analyzes text in under 1 millisecond ⚡
- **Memory**: Tiny footprint - runs on any computer 💾
- **Scalability**: Easy to include other languagues 📈



### What You Need
- Python 3.7+ 🐍
- NumPy (for the math magic) 🔢


### Setup the project
```bash
git clone [your-repo]
pip install numpy
python trainModel.py  # Train your AI
python runModel.py    # Test it out!
```




