

def solution(genres, plays):
    answer = []
    
    N = len(genres)
    
    musics = {}
    for idx in range(N):
        genre = genres[idx]
        play = plays[idx]
        
        if genre not in musics:
            musics[genre] = [play, (play, idx)]
        else:
            musics[genre][0] += play
            musics[genre].append((play, idx))
            
    albums = []
    for genre in musics:
        play = musics[genre][0]
        music = sorted(musics[genre][1:])
        albums.append([genre, play, music])
    
    albums = sorted(albums, key=lambda elmt: -elmt[1])
    for album in albums:
        album = sorted(album[2], key=lambda elmt: -elmt[0])
        
        answer.append(album[0][1])
        if len(album) >= 2:
            answer.append(album[1][1])
    
    return answer