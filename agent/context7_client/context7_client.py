import random

class Context7Client:
    """
    A client to connect to and interact with the Context7 MCP server.
    This is a mocked implementation for demonstration purposes.
    """
    def __init__(self, base_url: str):
        """
        Initializes the client with the server's base URL.
        """
        self.base_url = base_url
        self.connected = False

    def connect(self) -> bool:
        """
        Establishes a mock connection to the MCP server.
        Has a 20% chance of failing to simulate network issues.
        """
        # In a real implementation, this would involve HTTP requests and health checks.
        if random.random() > 0.2: # 80% chance of success
            self.connected = True
            print("Successfully connected to Context7 MCP server.")
            return True
        else:
            self.connected = False
            print("Failed to connect to Context7 MCP server.")
            return False

    def get_enhanced_explanation(self, topic: str) -> str | None:
        """
        Fetches a mock detailed, enhanced explanation for a given topic.
        """
        if not self.connected:
            return "Error: Not connected to Context7 MCP server."
        
        # Mocked response
        mock_explanations = {
            "mitochondria": "The mitochondria is the powerhouse of the cell. It generates most of the cell's supply of adenosine triphosphate (ATP), used as a source of chemical energy.",
            "photosynthesis": "Photosynthesis is a process used by plants, algae, and certain bacteria to harness energy from sunlight into chemical energy.",
        }
        
        return mock_explanations.get(topic.lower(), f"Sorry, I don't have an enhanced explanation for '{topic}'.")

    def get_related_topics(self, topic: str) -> list[str] | None:
        """
        Retrieves a mock list of topics related to the input topic.
        """
        if not self.connected:
            return None
        
        # Mocked response
        mock_related_topics = {
            "mitochondria": ["Cellular Respiration", "ATP", "Endosymbiotic Theory"],
            "photosynthesis": ["Chlorophyll", "Carbon Cycle", "Plant Biology"],
        }
        
        return mock_related_topics.get(topic.lower())
