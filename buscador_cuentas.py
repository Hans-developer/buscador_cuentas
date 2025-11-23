import sys
import requests  # Asegúrate de que esto esté aquí para evitar errores

# Comprobar si se proporcionó un nombre de usuario
if len(sys.argv) != 2:
    print("\033[31mUso: python3 script.py <nombre_de_usuario>\033[0m")  # Rojo para el mensaje de uso
    sys.exit(1)

# Nombre de usuario a buscar
USERNAME = sys.argv[1]

# Archivo de resultados
RESULTS_FILE = f"{USERNAME}.txt"

# Lista de sitios web para buscar (100 enlaces)
SITES = [
    f"https://twitter.com/{USERNAME}",
    f"https://www.instagram.com/{USERNAME}",
    f"https://www.facebook.com/{USERNAME}",
    f"https://www.linkedin.com/in/{USERNAME}",
    f"https://github.com/{USERNAME}",
    f"https://www.reddit.com/user/{USERNAME}",
    f"https://www.tiktok.com/@{USERNAME}",
    f"https://www.pinterest.com/{USERNAME}",
    f"https://www.snapchat.com/add/{USERNAME}",
    f"https://www.tumblr.com/blog/{USERNAME}",
    f"https://www.quora.com/profile/{USERNAME}",
    f"https://stackoverflow.com/users/search?q={USERNAME}",
    f"https://www.xda-developers.com/member.php?u={USERNAME}",
    f"https://www.deviantart.com/{USERNAME}",
    f"https://www.goodreads.com/user/show/{USERNAME}",
    f"https://www.myspace.com/{USERNAME}",
    f"https://www.flickr.com/photos/{USERNAME}",
    f"https://www.behance.net/{USERNAME}",
    f"https://www.dribbble.com/{USERNAME}",
    f"https://www.500px.com/{USERNAME}",
    f"https://medium.com/@{USERNAME}",
    f"https://www.blogger.com/profile/{USERNAME}",
    f"https://wordpress.com/{USERNAME}",
    f"https://www.livejournal.com/users/{USERNAME}",
    f"https://www.wix.com/{USERNAME}",
    f"https://steamcommunity.com/id/{USERNAME}",
    f"https://www.playstation.com/en-us/community/user/{USERNAME}",
    f"https://www.xbox.com/en-US/search?q={USERNAME}",
    f"https://www.bungie.net/en/Profile/{USERNAME}",
    f"https://www.behance.net/{USERNAME}",
    f"https://www.upwork.com/o/profiles/users/_~0123456789abcdefg/{USERNAME}",
    f"https://www.freelancer.com/u/{USERNAME}",
    f"https://www.fiverr.com/{USERNAME}",
    f"https://www.last.fm/user/{USERNAME}",
    f"https://www.soundcloud.com/{USERNAME}",
    f"https://www.spotify.com/{USERNAME}",
    f"https://www.youtube.com/user/{USERNAME}",
    f"https://www.vimeo.com/{USERNAME}",
    f"https://www.twitch.tv/{USERNAME}",
    f"https://www.etsy.com/shop/{USERNAME}",
    f"https://www.craigslist.org/about/sites#US",
    f"https://www.angieslist.com/companylist/us/{USERNAME}.htm",
    f"https://www.yellowpages.com/search?search_terms={USERNAME}",
    f"https://www.whitepages.com/name/{USERNAME}",
    f"https://www.patreon.com/{USERNAME}",
    f"https://www.twitch.tv/{USERNAME}",
    f"https://www.reverbnation.com/{USERNAME}",
    f"https://www.soundclick.com/bands/default.cfm?bandID={USERNAME}",
    f"https://www.bandcamp.com/{USERNAME}",
    f"https://www.goodreads.com/user/show/{USERNAME}",
    f"https://www.minds.com/{USERNAME}",
    f"https://www.4chan.org/user/{USERNAME}",
    f"https://www.fanfiction.net/u/{USERNAME}",
    f"https://www.wattpad.com/user/{USERNAME}",
    f"https://www.ravelry.com/users/{USERNAME}",
    f"https://www.furaffinity.net/user/{USERNAME}",
    f"https://www.kickstarter.com/profile/{USERNAME}",
    f"https://www.indiegogo.com/individuals/{USERNAME}",
    f"https://www.couchsurfing.com/people/{USERNAME}",
    f"https://www.eventbrite.com/user/{USERNAME}",
    f"https://www.meetup.com/members/{USERNAME}",
    f"https://www.angieslist.com/companylist/us/{USERNAME}.htm",
    f"https://www.zillow.com/profile/{USERNAME}/",
    f"https://www.tripadvisor.com/Profile/{USERNAME}",
    f"https://www.yelp.com/user_details?userid={USERNAME}",
    f"https://www.etsy.com/shop/{USERNAME}",
    f"https://www.bing.com/search?q={USERNAME}",
    f"https://www.google.com/search?q={USERNAME}",
    f"https://www.linkedin.com/in/{USERNAME}",
    f"https://www.imdb.com/user/ur{USERNAME}",
    f"https://www.merchbar.com/{USERNAME}",
    f"https://www.scribd.com/user/{USERNAME}",
    f"https://www.artstation.com/{USERNAME}",
    f"https://www.9gag.com/u/{USERNAME}",
    f"https://www.quora.com/profile/{USERNAME}",
    f"https://www.scoop.it/u/{USERNAME}",
    f"https://www.untappd.com/user/{USERNAME}",
    f"https://www.last.fm/user/{USERNAME}",
    f"https://www.soundcloud.com/{USERNAME}",
    f"https://www.spotify.com/user/{USERNAME}",
    f"https://www.youtube.com/user/{USERNAME}",
    f"https://www.vimeo.com/user/{USERNAME}",
    f"https://www.twitch.tv/{USERNAME}",
    f"https://www.fiverr.com/{USERNAME}",
    f"https://www.upwork.com/o/profiles/users/_~{USERNAME}/",
    f"https://www.freelancer.com/u/{USERNAME}",
    f"https://www.indeed.com/q-{USERNAME}-jobs.html",
    f"https://www.glassdoor.com/Profiles/{USERNAME}.htm",
    f"https://www.careerbuilder.com/profile/{USERNAME}",
    f"https://www.hired.com/user/{USERNAME}",
    f"https://www.simplyhired.com/search?q={USERNAME}",
    f"https://www.jobcase.com/profile/{USERNAME}",
    f"https://www.ziprecruiter.com/candidate/profile/{USERNAME}",
]

# Inicializar el archivo de resultados
with open(RESULTS_FILE, 'w') as results_file:
    results_file.write(f"Resultados de búsqueda para: {USERNAME}\n")
    results_file.write("======================================\n")

# Función para buscar el nombre de usuario en los sitios
def buscar_usuario():
    for site in SITES:
        print(f"\033[32mBuscando en: {site}\033[0m")  # Verde para la búsqueda
        try:
            response = requests.get(site)
            if USERNAME in response.text:
                print(f"\033[33m¡Encontrado en: {site}!\033[0m")  # Amarillo para encontrado
                with open(RESULTS_FILE, 'a') as results_file:
                    results_file.write(f"Encontrado en: {site}\n")  # Guardar en el archivo
            else:
                print(f"\033[31mNo encontrado en: {site}\033[0m")  # Rojo para no encontrado
        except requests.RequestException as e:
            print(f"\033[31mError al acceder a: {site} - {e}\033[0m")  # Rojo para error

# Llamar a la función de búsqueda
buscar_usuario()

# Mensaje final
print(f"\033[32mBúsqueda completada. Resultados guardados en: {RESULTS_FILE}\033[0m")
