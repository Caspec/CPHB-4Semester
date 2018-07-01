package rpn;

public class Calculator implements Operation {

    public Calculator() {
    }

    @Override
    public Integer operationAdd(Integer operation1, Integer operation2) {
        return operation1 + operation2;
    }

    @Override
    public Integer operationMinus(Integer operation1, Integer operation2) {
        return operation1 - operation2;
    }

    @Override
    public Integer operationMulti(Integer operation1, Integer operation2) {
        return operation1 * operation2;
    }

    @Override
    public Integer operationDiv(Integer operation1, Integer operation2) {
        return operation1 / operation2;
    }

}
