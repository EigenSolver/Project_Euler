using DelimitedFiles

# GLOBAL PARAMS
mat=readdlm("p081_matrix.txt", ',')
m,n=size(mat)
#i, j  row col

function minpath(col0::Vector,col1::Vector,i)::Number
    pathsum=col0[i]+col1[i]
    for k in 1:i-1
        p=min(col0[k]+sum(col1[k:i]),sum(col0[k:i])+col1[i])
        if p<pathsum
            pathsum=p
        end
    end
    for k in i+1:m
        p=min(col0[k]+sum(col1[i:k]),sum(col0[i:k])+col1[i])
        if p<pathsum
            pathsum=p
        end
    end
    return pathsum
end

function movecolumn(col0::Vector, col1::Vector)::Vector
    # start column 0, end col 1
    # @assert size(col0)==size(col1)
    n=length(col0)
    col=zeros(n)
    for i in 1:n
        col[i]=minpath(col0,col1,i)
    end
    return col
end

function recursivepath(mat::Matrix)
    for j in 2:n
        mat[:,j]=movecolumn(mat[:,j-1],mat[:,j])
    end
end

# mat= [131 673 234 103 18; 
# 201 96 342 965 150;
# 630 803 746 422 111;
# 537 699 497 121 956;
# 805 732 524 37 331]
# m,n=size(mat)


recursivepath(mat)
println(minimum(mat[:,end]))