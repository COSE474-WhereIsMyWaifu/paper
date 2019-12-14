#!/bin/bash

xelatex final.tex && bibtex final.aux && xelatex final.tex
