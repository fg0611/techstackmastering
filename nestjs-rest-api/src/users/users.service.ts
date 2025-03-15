import { Injectable } from '@nestjs/common'

@Injectable()
export class UsersService {
    private users = [{ id: 1, name: 'chiqui' }, { id: 2, name: 'negra' }]

findAll() {return this.users}

}