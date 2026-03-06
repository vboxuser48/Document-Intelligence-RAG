def search(index,model,question,chunks,k=3):

    question_embedding=model.encode([question])
    distance,indices=index.search(question_embedding,k)
    results=[]
    unique_indices = list(dict.fromkeys(indices[0]))

    for i in unique_indices:
        results.append(chunks[i])

    return results