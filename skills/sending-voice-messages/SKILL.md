---
name: sending-voice-messages
description: Use when sending spoken replies, especially on Telegram where exactly one voice-note output is required with language-matched voice selection and no duplicate audio delivery.
---

# Sending Voice Messages

## Overview
Send voice replies reliably: correct language voice, exactly one Telegram voice note, no duplicate MP3/voice pairs.

**REQUIRED SKILL:** Use `edge-tts` for audio generation.

## Language-to-Voice Mapping (default)
- German text (`de`) → `de-DE-KatjaNeural`
- English text (`en`) → `en-US-MichelleNeural`
- If language is unclear: use the language of the user’s message.

## Telegram Single-Output Rule (critical)
For Telegram voice replies, always do this sequence:

1. Generate audio with Edge-TTS (prefer explicit `--voice` based on language)
2. Send audio only once via `message.send` with `asVoice=true`
3. Return `NO_REPLY` in assistant output to prevent duplicate delivery

## Hard Never Rules
- Never post both MP3 file and voice note for the same reply.
- Never reply with `[[audio_as_voice]]` + `MEDIA:` when you already sent the audio via `message.send`.
- Never forward raw `tts` tool output directly into chat when single voice-note delivery is required.

## Quick Execution Pattern
```bash
# 1) Render audio with explicit voice
node /home/seb/code/superpowers/skills/edge-tts/scripts/tts-converter.js \
  "<text>" \
  --voice de-DE-KatjaNeural \
  --output /tmp/voice-note.mp3
```

```json
// 2) Send exactly one voice note
{
  "action": "send",
  "channel": "telegram",
  "target": "<chat-id>",
  "media": "/tmp/voice-note.mp3",
  "asVoice": true
}
```

Then assistant response: `NO_REPLY`.

## Troubleshooting

### Symptom: `NO` appears briefly (or sticks) during silent voice-only turns
Root cause: Telegram preview streaming can leak the beginning of `NO_REPLY` in some partial-stream paths.

Fix (keep preview enabled):
- Use `channels.telegram.streamMode: "block"`
- Set `channels.telegram.draftChunk.minChars: 200` (or higher)
- Keep `NO_REPLY` replies short and exact for message-tool voice sends

### Symptom: wrong language voice
Fix:
- Always force explicit voice in generation command (e.g. `--voice de-DE-KatjaNeural` for German).
- Do not rely on implicit defaults.

## Verification Checklist
- [ ] Voice language matches text language
- [ ] Exactly one audio delivered in Telegram
- [ ] No duplicate MP3 + voice-note pair
- [ ] No transient `NO` text appears
- [ ] Assistant replied with `NO_REPLY` after `message.send`
