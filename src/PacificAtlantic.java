// No. 417

import java.util.ArrayList;
import java.util.List;

public class PacificAtlantic {
    private int[][] direction = {{1,0},{-1,0},{0,1},{0,-1}};

    public List<int[]> pacificAtlantic(int[][] matrix) {
        List<int[]> result = new ArrayList<>();

        // 设置P和A两个矩阵，联合查询
        int m = matrix.length;
        if (m==0)
            return result;
        int n = matrix[0].length;
        int pVisited[][] = new int[m][n];
        int aVisited[][] = new int[m][n];
        // 初始化
        for(int i=0; i<m; i++) {
            for (int j = 0; j < n; j++) {
                pVisited[i][j] = 0;
                aVisited[i][j] = 0;
            }
        }

        for (int i=0; i<m; i++) {
            dfs(matrix, i, 0, pVisited, m, n);
            dfs(matrix, i, n-1, aVisited, m, n);
        }

        for (int j=0; j<n; j++) {
            dfs(matrix, 0, j, pVisited, m, n);
            dfs(matrix, m-1, j, aVisited, m, n);
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (pVisited[i][j]==1 && aVisited[i][j]==1)
                    result.add(new int[]{i, j});
            }
        }
        return result;
    }

    public void dfs(int[][] mat, int i, int j, int[][] visited, int m, int n) {
        visited[i][j] = 1;
        for(int[] dir:this.direction) {
            //System.out.println(dir[0]);
            int x = i + dir[0];
            int y = j + dir[1];
            // 从低往高遍历，最后在合并即得到最高到低的通路
            if (x<0 || x>=m || y<0 || y>=n || visited[x][y]==1 || mat[x][y]<mat[i][j]) {
                continue;
            }
//            System.out.print(x);
//            System.out.print(y);
//            System.out.print(" ");
            this.dfs(mat, x, y, visited, m, n);
        }
    }

    public static void main(String[] args) {
        int[][] mat = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
        List<int[]> temp = new PacificAtlantic().pacificAtlantic(mat);
        for (int[] x: temp) {
            System.out.print(x[0]);
            System.out.print(x[1]);
            System.out.print("\n");
        }
    }
}
