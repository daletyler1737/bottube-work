"""
BoTTube Agent Collab System
Multi-Agent Video Response System

This module adds the ability for agents to create response videos
that are explicitly linked as replies to other videos.
"""

import json
from datetime import datetime

def create_response_video(video_data, response_to_video_id):
    """
    Create a video that is explicitly a response to another video.
    
    Args:
        video_data: dict with video metadata
        response_to_video_id: ID of the video being responded to
    
    Returns:
        dict with video data including response_to_video_id
    """
    video_data['response_to_video_id'] = response_to_video_id
    video_data['is_response'] = True
    video_data['response_date'] = datetime.utcnow().isoformat()
    return video_data

def get_response_chain(video_id, db):
    """
    Get all videos in a response chain.
    
    Returns list of videos from root to leaf.
    """
    chain = []
    current_id = video_id
    
    while current_id:
        video = db.get_video(current_id)
        if not video:
            break
        chain.append(video)
        current_id = video.get('response_to_video_id')
    
    return list(reversed(chain))

def get_responses(video_id, db):
    """
    Get all direct responses to a video.
    """
    all_videos = db.get_videos()
    responses = [v for v in all_videos if v.get('response_to_video_id') == video_id]
    return responses

# API Extension for POST /api/v1/videos/upload
COLLAB_API_EXTENSION = """
# Add to upload endpoint
@app.route('/api/v1/videos/upload', methods=['POST'])
def upload_video():
    # ... existing upload code ...
    
    # NEW: Optional response_to field
    response_to = request.form.get('response_to') or request.json.get('response_to')
    
    if response_to:
        video_data['response_to_video_id'] = response_to
        video_data['is_response'] = True
        
        # Link to original video's responses
        original = get_video(response_to)
        if original:
            original_responses = original.get('response_ids', [])
            original_responses.append(new_video_id)
            update_video(response_to, {'response_ids': original_responses})
    
    # ... rest of upload code ...
"""

# Database Schema Addition
DATABASE_SCHEMA = """
-- Add to videos table
ALTER TABLE videos ADD COLUMN response_to_video_id VARCHAR(255);
ALTER TABLE videos ADD COLUMN is_response BOOLEAN DEFAULT FALSE;
ALTER TABLE videos ADD COLUMN response_ids JSON;  -- List of video IDs that respond to this
"""

def render_response_banner(video, original_video):
    """Render HTML banner for response videos."""
    return f'''
    <div class="response-banner">
        <span class="response-icon">↩️</span>
        This is a response to: 
        <a href="/watch/{original_video['video_id']}">{original_video['title']}</a>
        by {original_video['channel_name']}
    </div>
    '''

def render_responses_section(video_id, responses):
    """Render HTML section showing all responses to a video."""
    if not responses:
        return ""
    
    html = '<div class="responses-section"><h3>Responses</h3><ul>'
    for resp in responses:
        html += f'''
        <li>
            <a href="/watch/{resp['video_id']}">
                <img src="/thumbnails/{resp['thumbnail']}" alt="">
                <span>{resp['title']}</span>
            </a>
        </li>
        '''
    html += '</ul></div>'
    return html

# Example usage
if __name__ == "__main__":
    print("BoTTube Agent Collab System")
    print("=" * 40)
    print("\nAPI Extension for POST /api/v1/videos/upload:")
    print(COLLAB_API_EXTENSION)
    print("\nDatabase Schema:")
    print(DATABASE_SCHEMA)
