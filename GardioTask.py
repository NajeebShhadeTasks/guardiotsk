from flask import Flask, request, jsonify
import requests
import csv
import os

app = Flask(__name__)

# Function to get Pokemon data from PokeAPI
def get_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "url": f"https://pokeapi.co/api/v2/pokemon/{data['id']}/",
            "base_stats": {
                "hp": data["stats"][0]["base_stat"],
                "attack": data["stats"][1]["base_stat"],
                "defense": data["stats"][2]["base_stat"],
                "special_attack": data["stats"][3]["base_stat"],
                "special_defense": data["stats"][4]["base_stat"],
                "speed": data["stats"][5]["base_stat"]
            }
        }
        return pokemon_info
    else:
        return None

# Function to save query to a CSV file
def save_query(pokemon_name, pokemon_info):
    file_exists = os.path.isfile('queries.csv')
    with open('queries.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "url", "hp", "attack", "defense", "special_attack", "special_defense", "speed"])
        writer.writerow([
            pokemon_info["name"],
            pokemon_info["url"],
            pokemon_info["base_stats"]["hp"],
            pokemon_info["base_stats"]["attack"],
            pokemon_info["base_stats"]["defense"],
            pokemon_info["base_stats"]["special_attack"],
            pokemon_info["base_stats"]["special_defense"],
            pokemon_info["base_stats"]["speed"]
        ])

@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    pokemon_name = request.args.get('name')
    if not pokemon_name:
        return jsonify({"error": "Please provide a pokemon name"}), 400
    
    pokemon_info = get_pokemon_data(pokemon_name)
    if pokemon_info:
        save_query(pokemon_name, pokemon_info)
        return jsonify(pokemon_info)
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
