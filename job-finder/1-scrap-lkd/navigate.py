import asyncio
import random as rd


async def generate_page(p, url):
    """Generates page object with anti-detection measures."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/135.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15",
        # Añade más User-Agents variados
    ]
    user_agent = rd.choice(user_agents)

    # Dimensiones de ventana realistas
    viewport_width = rd.randint(1280, 1920)
    viewport_height = rd.randint(720, 1080)

    browser = await p.chromium.launch(
        headless=False,  # Mantener False para desarrollo, True para producción (con cuidado)
        args=[
            "--disable-blink-features=AutomationControlled"
        ],  # Intenta deshabilitar flags de automatización
    )
    context = await browser.new_context(
        user_agent=user_agent,
        viewport={"width": viewport_width, "height": viewport_height},
        # Configuración de cookies (puedes cargar cookies guardadas aquí si es necesario)
    )
    page = await context.new_page()

    # ... dentro de generate_page ...
    language_preferences = [
        # ["en-US", "en"],
        ["es-AR", "es"],
        ["es", "en-US", "en"],
        # ["pt-BR", "pt", "en-US", "en"],
        # ... más combinaciones realistas ...
    ]

    lang = rd.choice(language_preferences)

    await page.evaluate("""() => {Object.defineProperty(navigator, 'languages', {get: () => JSON.stringify(""" + f"""{lang}""" + """)})}""")

    # Inyectar JavaScript para eliminar navigator.webdriver y otros indicios
    await page.evaluate(
        """() => {
        delete navigator.webdriver;
        // Simular la propiedad plugins (puede ser complejo simularla completamente)
        if (navigator.plugins) {
            // Puedes intentar simular una lista de plugins comunes
            navigator.plugins.length = 5;
            navigator.plugins.item = (index) => ({ name: 'Shockwave Flash', description: 'Adobe Flash plugin', enabledPlugin: '...' });
            navigator.plugins.namedItem = (name) => (name === 'Shockwave Flash' ? { name: 'Shockwave Flash', description: 'Adobe Flash plugin', enabledPlugin: '...' } : null);
        }       
        // Simular la propiedad languages
    }"""
    )

    #     Object.defineProperty(navigator, 'languages', {
    #         get: () => ['en-US', 'en']
    #     });

    await page.goto(url)
    return page, browser


async def scroll_randomly(page, min_scroll=100, max_scroll=300, num_scrolls=1):
    """execute random scrolls"""
    for _ in range(num_scrolls):
        scroll_amount = rd.randint(min_scroll, max_scroll)
        await page.evaluate(f"window.scrollBy(0, {scroll_amount})")
        await asyncio.sleep(rd.uniform(0.5, 1.3))  # Pausa aleatoria entre scrolls
