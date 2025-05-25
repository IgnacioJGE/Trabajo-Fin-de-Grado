#!/bin/bash

rasa run --enable-api --cors "*" -p 5005  &
rasa run actions --actions actions --cors "*" -p 5055 