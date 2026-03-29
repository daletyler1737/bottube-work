"""
BoTTube Parasocial Hooks
Agents That Notice Their Audience

This module adds audience awareness to BoTTube agents,
enabling them to acknowledge regular viewers and commenters.
"""

import json
from datetime import datetime, timedelta
from collections import defaultdict

def track_viewer_activity(viewer_id, video_id, action='view'):
    """
    Track viewer activity across videos.
    
    Returns dict with:
    - is_regular: True if viewer commented on 3+ videos
    - is_new: True if first comment ever
    - comment_count: Total comments
    - videos_viewed: List of video IDs
    """
    # In production, this would query the database
    # For now, return mock data structure
    return {
        'viewer_id': viewer_id,
        'videos_commented': ['vid1', 'vid2'],  # Would come from DB
        'comment_count': 2,
        'is_regular': False,
        'is_new': True,
        'last_seen': datetime.utcnow().isoformat()
    }

def generate_agent_response(viewer, video_id):
    """
    Generate agent response text based on viewer relationship.
    """
    if viewer['is_new']:
        return f"Welcome! Great to have you here for the first time! 💫"
    
    if viewer['is_regular']:
        return f"Good to see you again, @{viewer['viewer_id']}! You've been here for {len(viewer['videos_commented'])} videos now! 🚀"
    
    return None  # No special response for casual viewers

def get_viewer_stats(agent_id):
    """
    Get aggregate stats for an agent's viewers.
    
    Returns:
    - total_unique_viewers
    - regular_commenters (3+ comments)
    - new_viewers (first comment)
    - top_viewers (by comment count)
    """
    return {
        'total_unique_viewers': 100,
        'regular_commenters': 15,
        'new_viewers': 23,
        'top_viewers': [
            {'viewer_id': 'user1', 'comments': 47},
            {'viewer_id': 'user2', 'comments': 31},
            {'viewer_id': 'user3', 'comments': 28}
        ]
    }

def render_viewer_badge(viewer):
    """Render badge HTML for viewer types."""
    if viewer.get('is_regular'):
        return '<span class="badge regular-viewer">⭐ Regular</span>'
    if viewer.get('is_new'):
        return '<span class="badge new-viewer">✨ First time!</span>'
    return ''

# Example response templates
REGULAR_VIEWER_TEMPLATES = [
    "Good to see you again, @{viewer}! You've been here since video {n}! 💜",
    "Hey @{viewer}! You're becoming a regular — love it! 🎉",
    "There's @{viewer} again! Welcome back! 👋",
]

NEW_VIEWER_TEMPLATES = [
    "Welcome to the stream, @{viewer}! Great to have you here! 🌟",
    "Hey @{viewer}, first time here? Welcome! 🎊",
    "A new face! @{viewer}, glad you could join! ✨",
]

SHARED_INTEREST_TEMPLATES = [
    "I notice @{viewer1} and @{viewer2} both commented on this — you're into the same stuff! 🤝",
]

def select_response_template(viewer, templates):
    """Select appropriate response template."""
    import random
    template = random.choice(templates)
    return template.format(
        viewer=viewer.get('viewer_id', 'friend'),
        n=len(viewer.get('videos_commented', [1,2,3]))
    )

# In production, this would integrate with the comment system
COMMENT_HOOK_TEMPLATE = '''
# Add to comment handling in bottube_server.py

def process_comment_with_hooks(comment_data):
    viewer_id = comment_data['user_id']
    video_id = comment_data['video_id']
    agent_id = comment_data['agent_id']
    
    # Track activity
    viewer = track_viewer_activity(viewer_id, video_id, 'comment')
    
    # Generate response
    response_text = generate_agent_response(viewer, video_id)
    
    if response_text:
        # Queue agent response with priority
        queue_agent_response(agent_id, response_text, priority='high')
    
    return {
        'comment': comment_data,
        'viewer': viewer,
        'agent_response': response_text
    }
'''

if __name__ == "__main__":
    print("BoTTube Parasocial Hooks")
    print("=" * 40)
    
    # Example usage
    viewer = track_viewer_activity('daletyler1737', 'vid123', 'comment')
    print(f"Viewer stats: {viewer}")
    
    response = generate_agent_response(viewer, 'vid123')
    print(f"Agent response: {response}")
