Progetto: API summary video + FE angular

tech stack:python - ffmpeg - pytorch

input: news video

-extract audio with python https://stackoverflow.com/questions/26741116/python-extract-wav-from-video-file

-extract text with time: https://colab.research.google.com/github/snakers4/silero-models/blob/master/examples.ipynb#scrollTo=QttWasy5hUd6

-crop video to summary: extract title or subtitle article word
crop the video where word are mentioned -10s +10s

----
part 2
-make a summary https://github.com/dmmiller612/bert-extractive-summarizer

-translate summary (optional): https://pypi.org/project/py-translate/

-create translated audio: https://github.com/mozilla/TTS

- remove speech voice from audio https://github.com/tsurumeso/vocal-remover/https://github.com/deezer/spleeter

- add translated audio