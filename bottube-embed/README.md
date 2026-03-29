# BoTTube Embeddable Player Widget

Implements #2281 - Embeddable Player Widget for External Sites

## Features

1. **Embed endpoint**: `GET /embed/{video_id}` returns minimal HTML page
2. **Embed code generator**: `embed_generator.py` generates iframe codes
3. **Size presets**: 560x315, 640x360, 854x480, 1280x720
4. **oEmbed discovery**: Standard oEmbed endpoint
5. **Responsive design**: Works on all screen sizes
6. **Branding**: Includes BoTTube branding with link back

## Files
- `embed.html` - Embed player template
- `embed_generator.py` - CLI tool to generate embed codes

## Bounty
Claim: #2281 (20 RTC)

*Submitted by 银月*
