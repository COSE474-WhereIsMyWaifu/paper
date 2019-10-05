#!/bin/bash

xelatex proposal.tex && bibtex proposal.aux && xelatex proposal.tex
