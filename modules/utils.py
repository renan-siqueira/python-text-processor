import asyncio


async def simulated_long_running_task(duration=5):
    """Simula uma tarefa de longa duração."""
    print("Iniciando tarefa demorada...")
    await asyncio.sleep(duration)
    print("Tarefa demorada concluída.")
    return "Resultado da tarefa"
