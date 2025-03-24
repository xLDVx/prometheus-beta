import json
import os
import time
from typing import List, Dict, Any

class MultipleChoiceLogger:
    """
    A class to log user responses to multiple-choice questions.
    
    Provides functionality to:
    - Log responses to a JSON file
    - Validate responses against question constraints
    - Handle different logging scenarios
    """
    
    def __init__(self, log_dir: str = 'logs'):
        """
        Initialize the logger with a specific log directory.
        
        Args:
            log_dir (str, optional): Directory to store log files. 
                                     Defaults to 'logs'.
        """
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        self.log_dir = log_dir
    
    def log_response(self, 
                     question_id: str, 
                     user_id: str, 
                     response: str, 
                     valid_options: List[str] = None) -> Dict[str, Any]:
        """
        Log a user's response to a multiple-choice question.
        
        Args:
            question_id (str): Unique identifier for the question
            user_id (str): Unique identifier for the user
            response (str): The selected response
            valid_options (List[str], optional): List of valid response options
        
        Returns:
            Dict[str, Any]: Log entry details
        
        Raises:
            ValueError: If response is invalid or parameters are incorrect
        """
        # Validate inputs
        if not question_id or not isinstance(question_id, str):
            raise ValueError("Invalid question_id. Must be a non-empty string.")
        
        if not user_id or not isinstance(user_id, str):
            raise ValueError("Invalid user_id. Must be a non-empty string.")
        
        if response is None:
            raise ValueError("Response cannot be None.")
        
        # Convert response to string to handle potential non-string inputs
        response = str(response)
        
        # Validate against valid options if provided
        if valid_options is not None:
            if not isinstance(valid_options, list):
                raise ValueError("valid_options must be a list of strings.")
            
            # Convert all valid options to strings 
            valid_options = [str(opt) for opt in valid_options]
            
            if response not in valid_options:
                raise ValueError(f"Invalid response. Must be one of {valid_options}")
        
        # Prepare log entry with current timestamp
        log_entry = {
            "question_id": question_id,
            "user_id": user_id,
            "response": response,
            "timestamp": time.time()
        }
        
        # Generate log filename
        log_filename = os.path.join(self.log_dir, f"{question_id}_responses.json")
        
        # Read existing log entries or create new list
        try:
            with open(log_filename, 'r') as f:
                log_entries = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            log_entries = []
        
        # Add new log entry
        log_entries.append(log_entry)
        
        # Write updated log entries
        with open(log_filename, 'w') as f:
            json.dump(log_entries, f, indent=2)
        
        return log_entry