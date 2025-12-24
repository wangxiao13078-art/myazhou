import { Chapter } from './types'

export const grade7Chapters: Chapter[] = [
  {
    id: 'z1',
    title: '专题一：有理数',
    techniques: [
      { id: 't1', title: '考法1：用分类讨论思想解数轴上的整点与动点问题', methodName: '分类讨论思想' },
      { id: 't2', title: '考法2：用归纳猜想解数轴上的规律探究问题', methodName: '归纳猜想' },
      { id: 't3', title: '考点2：比较有理数大小常用的方法', methodName: '比较法' },
      { id: 't4', title: '考法1：绝对值的性质及其运用', methodName: '绝对值性质' },
      { id: 't5', title: '考法2：几何意义的运用', methodName: '几何意义' },
      { id: 't6', title: '考点4：有理数的新定义问题', methodName: '新定义' },
      { id: 't7', title: '考点5：有理数的实际应用', methodName: '实际应用' },
    ]
  },
  {
    id: 'z2',
    title: '专题二：有理数的运算',
    techniques: [
      { id: 't8', title: '考法1：拼凑法', methodName: '混合运算' },
      { id: 't9', title: '考法2：裂项法', methodName: '混合运算' },
      { id: 't10', title: '考法3：倒数法和运算律', methodName: '混合运算' },
      { id: 't11', title: '考法4：混合运算', methodName: '混合运算' },
      { id: 't12', title: '考法1：数轴上的折叠问题', methodName: '折叠模型' },
      { id: 't13', title: '考法2：用分类讨论思想解数轴与有理数运算相关的动点问题', methodName: '分类讨论' },
      { id: 't14', title: '考点3：有理数的运算与绝对值的综合运用', methodName: '分类讨论' },
      { id: 't15', title: '考点4：与有理数运算相关的新定义问题', methodName: '化归思想' },
    ]
  },
  {
    id: 'z3',
    title: '专题三：代数式',
    techniques: [
      { id: 't16', title: '考点1：用字母表示数', methodName: '代数基础' },
      { id: 't17', title: '考法1：直接求代数式的值', methodName: '代数式求值' },
      { id: 't18', title: '考法2：整体思想求代数式的值', methodName: '整体思想' },
      { id: 't19', title: '考点3：用归纳猜想解代数式中的规律探究问题', methodName: '归纳猜想' },
      { id: 't20', title: '考点4：代数式的新定义问题', methodName: '新定义' },
    ]
  },
  {
    id: 'z4',
    title: '专题四：整式的加减',
    techniques: [
      { id: 't21', title: '考点1：利用整体思想化简求值', methodName: '整体思想' },
      { id: 't22', title: '考法1：利用数轴化简绝对值', methodName: '数形结合' },
      { id: 't23', title: '考法2：利用分类讨论思想化简绝对值', methodName: '分类讨论' },
      { id: 't24', title: '考点3：用转化思想解整式的加减中的新定义问题', methodName: '转化思想' },
    ]
  },
  {
    id: 'z5',
    title: '专题五：一元一次方程',
    techniques: [
      // 考点1：用数学思想解一元一次方程
      { id: 't25', title: '【考点1】考法1：用整体思想解一元一次方程', methodName: '整体思想' },
      { id: 't26', title: '【考点1】考法2：用特殊化与一般化思想解一元一次方程（裂项相消法）', methodName: '裂项相消' },
      { id: 't27', title: '【考点1】考法3：用分类讨论思想解含绝对值的一元一次方程', methodName: '分类讨论' },
      // 考点2：与解一元一次方程有关的参数问题
      { id: 't38', title: '【考点2】考法1：两个一元一次方程解的关系', methodName: '参数问题' },
      { id: 't39', title: '【考点2】考法2：一元一次方程的错解问题', methodName: '错解问题' },
      { id: 't40', title: '【考点2】考法3：整数解问题', methodName: '整数解' },
      // 考点3：用转化思想解新定义问题
      { id: 't41', title: '【考点3】用转化思想解新定义问题', methodName: '转化思想' },
      // 考点4：一元一次方程应用题
      { id: 't42', title: '【考点4】考法1：调配与配套问题', methodName: '调配配套' },
      { id: 't43', title: '【考点4】考法2：工程问题', methodName: '工程问题' },
      { id: 't44', title: '【考点4】考法3：行程问题', methodName: '行程问题' },
      { id: 't28', title: '【考点4】考法4：销售利润问题', methodName: '销售利润' },
      { id: 't29', title: '【考点4】考法5：分段计费问题', methodName: '分段计费' },
      { id: 't30', title: '【考点4】考法6：方案选择问题', methodName: '方案选择' },
      { id: 't31', title: '【考点4】考法7：古代数学问题', methodName: '古代数学' },
    ]
  },
  {
    id: 'z6',
    title: '专题六：几何图形初步',
    techniques: [
      // 考点1：数学思想在线段计算中的应用
      { id: 't32', title: '【考点1】考法1：整体思想', methodName: '整体思想' },
      { id: 't33', title: '【考点1】考法2：方程思想', methodName: '方程思想' },
      { id: 't34', title: '【考点1】考法3：分类讨论思想', methodName: '分类讨论' },
      { id: 't35', title: '【考点1】考法4：数形结合思想', methodName: '数形结合' },
      // 考点2：数学思想在角度计算中的应用
      { id: 't36', title: '【考点2】考法1：整体思想', methodName: '整体思想' },
      { id: 't37', title: '【考点2】考法2：方程思想', methodName: '方程思想' },
    ]
  }
]
