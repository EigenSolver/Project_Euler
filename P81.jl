using DelimitedFiles

mat=readdlm("p081_matrix.txt", ',')

function lastmove(i::Int, j::Int, mat::Matrix)
    if i*j==1
        return 0
    elseif i==1
        return mat[i, j-1]
    elseif j==1
        return mat[i-1, j]
    else
        return min(mat[i-1, j], mat[i, j-1])
    end
end

function recursivepath(mat::Matrix)
    m,n= size(mat)
    for i in 1:m
        for j in 1:n
            mat[i,j]+=lastmove(i,j,mat)
        end
    end
end

mat= [131 673 234 103 18; 
201 96 342 965 150;
630 803 746 422 111;
537 699 497 121 956;
805 732 524 37 331]
recursivepath(mat)
println(mat[end,end])