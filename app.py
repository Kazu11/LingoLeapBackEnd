from flask import Flask, request, render_template
from flask_cors import CORS
import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

