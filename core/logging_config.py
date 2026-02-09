import logging
import sys
from pathlib import Path
from datetime import datetime
import json

class MASLLogger:
    """Enhanced logging system for MASL"""
    
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup main logger
        self.logger = logging.getLogger("MASL")
        self.logger.setLevel(logging.DEBUG)
        
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            datefmt='%H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler for detailed logs
        log_file = self.log_dir / f"masl_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # JSON handler for structured logging
        json_file = self.log_dir / f"masl_structured_{datetime.now().strftime('%Y%m%d')}.jsonl"
        self.json_handler = StructuredJSONHandler(json_file)
        self.logger.addHandler(self.json_handler)
    
    def log_experiment_start(self, experiment_id: str, problem: str):
        """Log experiment start"""
        self.logger.info(f"🧪 Started experiment {experiment_id}: {problem}")
    
    def log_agent_action(self, agent_name: str, action: str, details: dict = None):
        """Log agent actions"""
        msg = f"🤖 {agent_name}: {action}"
        if details:
            msg += f" | Details: {json.dumps(details, default=str)}"
        self.logger.info(msg)
    
    def log_error(self, component: str, error: Exception, context: dict = None):
        """Log errors with context"""
        error_msg = f"❌ {component}: {str(error)}"
        if context:
            error_msg += f" | Context: {json.dumps(context, default=str)}"
        self.logger.error(error_msg, exc_info=True)
    
    def log_performance(self, operation: str, duration: float, metadata: dict = None):
        """Log performance metrics"""
        perf_msg = f"⚡ {operation}: {duration:.2f}s"
        if metadata:
            perf_msg += f" | {json.dumps(metadata, default=str)}"
        self.logger.info(perf_msg)

class StructuredJSONHandler(logging.Handler):
    """Custom handler for structured JSON logging"""
    
    def __init__(self, filename):
        super().__init__()
        self.filename = Path(filename)
    
    def emit(self, record):
        try:
            log_entry = {
                'timestamp': datetime.fromtimestamp(record.created).isoformat(),
                'level': record.levelname,
                'logger': record.name,
                'message': record.getMessage(),
                'module': record.module,
                'function': record.funcName,
                'line': record.lineno
            }
            
            if record.exc_info:
                log_entry['exception'] = self.formatException(record.exc_info)
            
            with open(self.filename, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
        except Exception:
            self.handleError(record)

# Global logger instance
masl_logger = MASLLogger()
