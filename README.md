[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/XzN-3LUi)
# Prompt 7: Visual Narrative/Language

> Rather than a 100% generative process, I like to think of this as a
>generative exosuit that carries me through the aesthetic process,
>presents me with algorithmically gathered material, and asks me to make
>certain decisions at a few key points and then amplifies those decisions
>into the final work.
>
> Greg Borenstein, process notes on "Generative Detective"

## Readings

### Practice

* ["The DALLE Image Generation"](https://platform.openai.com/docs/guides/images/usage)
* [LLaVa](https://ollama.com/library/llava)

## Summary

This week, we delve deeper into the concept of visual narrative, exploring how visual storytelling elements are created, interpreted, and enhanced through the use of LLMs. Visual narratives have long been a vital means of communication, combining imagery and context to convey complex ideas, emotions, and stories that transcend language barriers. Your task is to examine how these models interpret prompts, craft visual narratives, and contribute to storytelling.

## Goals

* Extending/refining our ability to practice prompt engineering to achieve specific higher-quality results
* Gaining an understanding of image narrative as a function/technology of time
* Discussing the ways in which models succeed or fail at creating equitable, fair, and representative stories
* Discovering other exploitable boundaries and what these offer

## Outcomes

* `1` text of at least `12` (panels) images integrated in the `narrative.md` document which:
  * communicates a narrative (i.e. story or plot) visually
* `1` text of a description/explanation of one image saved in `image_explanation` file
* entries of prompts used in the [prompt_journal.md](writing/prompt_journal.md) 

## Process

This assignment requires you to use the OpenAI and/or LLaVA library to access image generation at the scale and quality we need. The implementation provided is complete but should be further enhanced to accommodate your work.

### Working in a VM

- Access your VM:
  -[pve1](https://pve1.cis.allegheny.edu:8006/)
  -[pve2](https://pve2.cis.allegheny.edu:8006/)
  -[pve3](https://pve3.cis.allegheny.edu:8006/)
- `ssh ubuntu@IP`
- To move the file from local: `scp ~/{path to local file} ubuntu@192.168.190.x:~/{local file}`
- Use GitHub (can set up ssh keys with `ssh-keygen`)
